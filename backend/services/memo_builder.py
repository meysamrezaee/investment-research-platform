# backend/services/memo_builder.py


def build_investment_prompt(
    company,
    financials,
    news,
    industry,
    risks,
    competitors
):

    prompt = f"""
    You are a senior investment analyst.

    Company:
    {company}

    Financial Analysis:
    {financials}

    News Analysis:
    {news}

    Industry Analysis:
    {industry}

    Risk Analysis:
    {risks}

    Competitor Analysis:
    {competitors}

    Create an investment memo with:

    1. Executive Summary
    2. Business Overview
    3. Financial Health
    4. Industry Position
    5. Key Risks
    6. Bull Case
    7. Bear Case
    8. Investment Conclusion

    Use professional equity research style.
    """

    return prompt