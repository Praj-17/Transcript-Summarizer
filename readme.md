# 🎙️ Transcript Summarizer

Leverage **Gemini** to summarize a given transcript file effortlessly!

## 🚀 Setup Instructions

### Option 1: Using Docker 🐳

Simplify your setup using Docker:

1. **Install Docker** on your system. If you haven't installed it yet, you can download it from [Docker's official website](https://www.docker.com/get-started).

2. **Pull the Docker image** from Docker Hub:
    ```bash
    docker pull prajwal1717/transcript_summarizer
    ```

3. **Run the Docker container**:
    ```bash
    docker run -d -p 5000:5000 --name transcript_summarizer -e GEMINI_API_KEY=YOUR_GEMINI_API_KEY prajwal1717/transcript_summarizer
    ```
    - 🔔 **Note**: Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

4. **Access the application**:
    - Open your browser and navigate to `http://localhost:5000/` to see the application running.

### Option 2: Manual Setup

1. **Install Python** (preferably version `3.12.3`).

2. **Install dependencies** using the following command:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    - Create a file named `.env` in your codebase.
    - Paste the following content into the `.env` file:
        ```env
        GEMINI_API_KEY=YOUR_GEMINI_API_KEY
        GEMINI_MODEL_NAME=gemini-1.5-flash
        SUMMARY_PROMPT_FILE_LOCATION=src/constants/summary_prompt.prompt
        ```
    - 🔔 **Note**: Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

## 📚 Documentation

### 🎯 Generate Transcript Summary

There is only a single endpoint: **`POST /earnings_transcript_summary`**

#### 📝 Input

The endpoint accepts form data:

1. **company_name** *(string)* - Name of the company.
2. **transcript_text** *(string)* - The transcript text.
3. **transcript_file** *(file)* - A PDF file as an alternative to the `transcript_text`.

#### 📤 Output

```json
{
  "company_name": "One 97 Communications Limited (Paytm)",
  "financial_performance": "Paytm reported strong financial performance in Q2FY25, with improved monetization of merchants and control over payment gateway costs leading to a higher net payment margin. The company also saw a material reduction in its cost base, exceeding its previous guidance for reductions in employee cost. Contribution margins have returned to near 55% without UPI incentives, which the company expects to be the new norm. The company's DLG model is also contributing to increased capital for credit disbursement to merchants, leading to higher margin business growth.",
  "market_dynamics": "The company sees a massive market opportunity in the personal loan distribution business and is focused on adding new lending partners to scale this segment. The company is also seeing strong demand in merchant lending, with a significant amount of capital being unlocked through DLG arrangements. The company notes that there is a cautious phase in the overall market cycle due to regulatory and market conditions.",
  "expansion_plans": "Paytm is focused on expanding its financial services business through new lending partners in personal loans and by unlocking more capital for merchant loans. The company is also exploring new secured loan products such as home loans and mortgages, but these are expected to have a more meaningful contribution in the future. The company is also exploring new advertising channels, including its Soundbox, but these are considered experimental and not expected to be a meaningful contributor to revenue in the near term.",
  "environmental_risks": "No information on environmental risks, sustainability, or ESG concerns was found in the transcript.",
  "regulatory_or_policy_changes": "The company is awaiting regulatory direction on the status of Paytm Payments Bank, which is currently under regulatory supervision. The company also notes that regulatory changes have impacted the UPI market, allowing Paytm to become a player in the UPI space. The company is waiting for approval from NPCI to onboard new customers under UPI."
}
```

## 📞 Contact Details

Like my work? Feel free to reach out!

- 📧 **Email**: [pwaykos1@gmail.com](mailto:pwaykos1@gmail.com)
- 📱 **Phone**: [+91 72495 42810](tel:+917249542810)
- 💼 **LinkedIn**: [Prajwal Waykos](https://www.linkedin.com/in/prajwal-waykos/)
- 📄 **Resume**: [View Resume](https://drive.google.com/file/d/1nk9R5xCP9nEcDYTDnNuLBVK4b81gKFPP/view?usp=drive_link)

Looking forward to connecting with you! 😊
