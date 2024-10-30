# Transcript Summarizer

uses gemini to summarize a given transcript file


## Setup instructions

1. install python preferrably python == `3.12.3`
2. install dependencies using the following command
    ```
    pip install -r requirements.txt
    ```
3. setup the env: create a file called `.env` in your code base and paste the following content there
    ```
    GEMINI_API_KEY = YOUR_GEMINI_API_KEY
    GEMINI_MODEL_NAME = gemini-1.5-flash
    summary_prompt_file_location = src\constants\summary_prompt.prompt
    ```
    
    `Note`: make sure you change `YOUR_GEMINI_API_KEY` to you actual key


## Documentation 
Generate transcript summary

There is only a single endpoint `/earnings_transcript_summary`

#### input

It accepts form input 

1. company_name - name of the company
2. transcript_text - transcript as a text
3. transcript_file - a pdf file as an alternative to the `transcript_text`

### output

```
{
"company_name": "One 97 Communications Limited (Paytm)",
"financial_performance": "Paytm reported strong financial performance in Q2FY25, with improved monetization of merchants
and control over payment gateway costs leading to a higher net payment margin. The company also saw a material reduction
in its cost base, exceeding its previous guidance for reductions in employee cost. Contribution margins have returned to
near 55% without UPI incentives, which the company expects to be the new norm. The company's DLG model is also
contributing to increased capital for credit disbursement to merchants, leading to higher margin business growth.",
"market_dynamics": "The company sees a massive market opportunity in the personal loan distribution business and is
focused on adding new lending partners to scale this segment. The company is also seeing strong demand in merchant
lending, with a significant amount of capital being unlocked through DLG arrangements. The company notes that there is a
cautious phase in the overall market cycle due to regulatory and market conditions.",
"expansion_plans": "Paytm is focused on expanding its financial services business through new lending partners in
personal loans and by unlocking more capital for merchant loans. The company is also exploring new secured loan products
such as home loans and mortgages, but these are expected to have a more meaningful contribution in the future. The
company is also exploring new advertising channels, including its Soundbox, but these are considered experimental and
not expected to be a meaningful contributor to revenue in the near term.",
"environmental_risks": "No information on environmental risks, sustainability, or ESG concerns was found in the
transcript.",
"regulatory_or_policy_changes": "The company is awaiting regulatory direction on the status of Paytm Payments Bank,
which is currently under regulatory supervision. The company also notes that regulatory changes have impacted the UPI
market, allowing Paytm to become a player in the UPI space. The company is waiting for approval from NPCI to onboard new
customers under UPI."
}
```