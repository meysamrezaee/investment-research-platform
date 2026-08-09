# backend/agents/industry_agent.py

import asyncio
from services.market_data import get_company_profile
from services.openai_client import ask_llm

async def analyze_industry(symbol: str) -> str:
    """
    Analyze the company's industry,
    market positioning, and trends.
    """

    profile = await asyncio.to_thread(
        get_company_profile,
        symbol
    )

    prompt = f"""
You are an investment research analyst.

Company:
{profile.get("companyName")}

Sector:
{profile.get("sector")}

Industry:
{profile.get("industry")}

Business Description:
{profile.get("description")}

Provide an industry analysis covering:

1. Industry overview
2. Industry growth drivers
3. Competitive landscape
4. Industry risks
5. Long-term outlook
6. Company's position within the industry

Keep the response under 300 words.
"""

    return await asyncio.to_thread(
        ask_llm,
        prompt
    )