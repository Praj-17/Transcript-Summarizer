from flask import Flask, request, jsonify
from pydantic import ValidationError
from src import SummaryModel  # Replace with actual import path for your SummaryModel
from src import PDFtoText, GeminiRunner
app = Flask(__name__)



app = Flask(__name__)
runner = GeminiRunner()

@app.route('/earnings_transcript_summary', methods=['POST'])
def earnings_transcript_summary():
    try:
        # Parse form data input
        company_name = request.form.get("company_name")
        transcript_text = request.form.get("transcript_text")

        # Input validation
        if not company_name or not transcript_text:
            return jsonify({"error": "Both 'company_name' and 'transcript_text' are required"}), 400
        # if len(transcript_text) > 20000:
        #     return jsonify({"error": "The 'transcript_text' exceeds the 20,000 token limit"}), 400

        # Analyze and summarize transcript text
        summary_data = runner.generate_summary_response(company_name, transcript_text)
        print(type(summary_data))
        
        # Validate and structure the response
        return summary_data

    except ValidationError as ve:
        return jsonify({"error": "Invalid input data", "details": ve.errors()}), 422
    except Exception as e:
        return jsonify({"error": "An error occurred during processing", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

