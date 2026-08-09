# backend/agents/financial-agent.py


import asyncio

from services.market_data import (
    get_company_data
)

from services.openai_client import (
    ask_llm
)


async def analyze_financials(
    symbol: str
):

    data = await asyncio.to_thread(
        get_company_data,
        symbol
    )

    prompt = f"""
Analyze the following company.

Company Profile:
{data['profile']}

Income Statement:
{data['income_statement']}

Balance Sheet:
{data['balance_sheet']}

Cash Flow Statement:
{data['cash_flow']}

Provide:

1. Revenue and profitability trends

2. Balance sheet strength
   - Cash position
   - Debt position
   - Liquidity

3. Cash flow quality
   - Operating cash flow
   - Free cash flow
   - Capital allocation

4. Financial strengths

5. Financial weaknesses

6. Overall financial health score (1-10)

Keep response under 500 words.
"""

    response = await asyncio.to_thread(
        ask_llm,
        prompt
    )

    return response