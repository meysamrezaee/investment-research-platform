# backend/agents/risk_agent.py

import asyncio
from services.market_data import get_company_data
from services.news_service import get_stock_news
from services.openai_client import ask_llm

async def analyze_risks(symbol: str) -> str:
    """
    Perform a risk assessment using
    company fundamentals and recent news.
    """
    company_data = await asyncio.to_thread(get_company_data, symbol)
    news = await asyncio.to_thread(get_stock_news, symbol)
    
    prompt = f"""
You are a senior risk analyst at an investment firm.

Company Profile:
{company_data['profile']}

Income Statement:
{company_data['income_statement']}

Balance Sheet:
{company_data['balance_sheet']}

Cash Flow Statement:
{company_data['cash_flow']}

Recent News:
{news}

Identify:

1. Business Risks
   - Product concentration
   - Customer concentration
   - Technology disruption

2. Financial Risks
   - Debt burden
   - Liquidity concerns
   - Cash flow weaknesses

3. Industry Risks
   - Competition
   - Industry cyclicality
   - Market saturation

4. Regulatory Risks
   - Antitrust
   - Privacy
   - Industry-specific regulation

5. Execution Risks
   - AI strategy execution
   - Acquisitions
   - Operational challenges

6. Overall Risk Rating
   - Low
   - Medium
   - High

7. Top 3 Risks Investors Should Monitor

Keep response under 400 words.

Be balanced.
Do not invent information.
Base conclusions on the supplied data.
"""

    return await asyncio.to_thread(
        ask_llm,
        prompt
    )