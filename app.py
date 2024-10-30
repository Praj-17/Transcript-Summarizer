from flask import Flask, request, jsonify,render_template_string
from pydantic import ValidationError
from src import SummaryModel  # Replace with actual import path for your SummaryModel
from src import PDFtoText, GeminiRunner
import markdown
import os
from werkzeug.utils import secure_filename



runner = GeminiRunner()
pdf_to_text = PDFtoText()

app = Flask(__name__)


@app.route('/earnings_transcript_summary', methods=['POST'])
def earnings_transcript_summary():
    try:
        # Parse form data input
        company_name = request.form.get("company_name")
        transcript_text = request.form.get("transcript_text")
        transcript_file = request.files.get("transcript_file")

        # Input validation
        if not company_name or (not transcript_text and not transcript_file):
            return jsonify({
                "error": "Both 'company_name' and either 'transcript_text' or 'transcript_file' are required"
            }), 400

        # If transcript_file is provided, save it to /data directory
        if transcript_file:
            # Check if the uploaded file is a PDF
            if transcript_file.filename.lower().endswith('.pdf'):
                # Ensure the /data directory exists
                data_dir = os.path.join(os.getcwd(), 'data')
                if not os.path.exists(data_dir):
                    os.makedirs(data_dir)

                # Sanitize the filename and define the file path
                filename = secure_filename(transcript_file.filename)
                file_path = os.path.join(data_dir, filename)

                # Save the uploaded file to the /data directory
                transcript_file.save(file_path)
                transcript_file.close()

                try:
                    # Pass the file path to extract_all_text function
                    transcript_text = pdf_to_text.extract_all_text(file_path)
                finally:
                    # Delete the file after processing
                    if os.path.exists(file_path):
                        os.remove(file_path)
            else:
                return jsonify({
                    "error": "Only PDF files are supported for 'transcript_file'"
                }), 400
        # Else, transcript_text should already be provided

        # Analyze and summarize transcript text
        summary_data = runner.generate_summary_response(company_name, transcript_text)

        # Return the summary data
        return summary_data

    except ValidationError as ve:
        return jsonify({
            "error": "Invalid input data",
            "details": ve.errors()
        }), 422
    except Exception as e:
        return jsonify({
            "error": "An error occurred during processing",
            "details": str(e)
        }), 500


@app.route('/', methods=['GET'])
def index():
    try:
        with open('README.md', 'r', encoding="utf-8") as f:
            md_content = f.read()
        # Convert markdown to HTML with extensions
        html_content = markdown.markdown(md_content, extensions=['fenced_code', 'codehilite'])

        # Define an HTML template with styles
        html_template = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Project README</title>
            <!-- Include Bootstrap CSS from CDN -->
            <link rel="stylesheet"
                  href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
                  integrity="sha384-JcKb8q3iqJ61gNVpCFMdZh"
                  crossorigin="anonymous">
            <!-- Include Highlight.js CSS for code syntax highlighting -->
            <link rel="stylesheet"
                  href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.2/styles/default.min.css">
            <style>
                body {
                    padding: 20px;
                    background-color: #f8f9fa;
                    font-family: 'Helvetica Neue', Arial, sans-serif;
                }
                .markdown-body {
                    max-width: 800px;
                    margin: 0 auto;
                }
                h1, h2, h3, h4, h5, h6 {
                    color: #343a40;
                    margin-top: 1.5em;
                    margin-bottom: 0.5em;
                }
                p {
                    color: #495057;
                    line-height: 1.7;
                }
                pre {
                    background-color: #f1f3f5;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                }
                code {
                    color: #e83e8c;
                    background-color: #f1f3f5;
                    padding: 2px 4px;
                    border-radius: 4px;
                }
                a {
                    color: #007bff;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
                ul, ol {
                    margin-left: 1.5em;
                }
                blockquote {
                    border-left: 5px solid #ced4da;
                    padding-left: 1em;
                    color: #6c757d;
                }
            </style>
        </head>
        <body>
            <div class="markdown-body">
                {{ content | safe }}
            </div>
            <!-- Include Highlight.js script -->
            <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.2/highlight.min.js"></script>
            <script>hljs.highlightAll();</script>
        </body>
        </html>
        '''

        # Render the HTML content within the template
        return render_template_string(html_template, content=html_content)
    except Exception as e:
        return jsonify({
            "error": "An error occurred while rendering the markdown file",
            "details": str(e)
        }), 500
if __name__ == '__main__':
    app.run(debug=True)

