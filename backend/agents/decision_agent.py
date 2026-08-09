# backend/agents/decision_agent.py

import asyncio
import json

from services.openai_client import ask_llm


async def generate_recommendation(
    company,
    financials,
    news,
    industry,
    risks,
    competitors
):

    prompt = f"""
You are a senior portfolio manager.

Based ONLY on the supplied evidence, produce valid JSON.

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

IMPORTANT:

- Return ONLY JSON.
- No markdown.
- No explanations outside JSON.
- Return EXACTLY 3 strengths.
- Return EXACTLY 3 risks.
- Sort strengths and risks from most important to least important.

Scoring Rules:

financial_score:
1-10
Measures profitability, cash generation, balance sheet quality, and financial resilience.

industry_score:
1-10
Measures attractiveness of the industry, secular growth trends, and long-term outlook.

competitive_score:
1-10
Measures competitive advantages, market position, switching costs, and moat strength.

safety_score:
1-10

10 = very safe
1 = very risky

confidence:
1-10
Represents confidence in the recommendation based on the available evidence.


DO NOT return key metrics.
Key metrics are generated separately by the application.

Return:

{{
  "financial_score": 1,

  "industry_score": 1,

  "competitive_score": 1,

  "safety_score": 1,

  "thesis": "...",

  "strengths": [
    "...",
    "...",
    "..."
  ],

  "risks": [
    "...",
    "...",
    "..."
  ],

  "upgrade_catalyst": "...",

  "downgrade_catalyst": "..."
}}

Return valid JSON only.
"""

    result = await asyncio.to_thread(
        ask_llm,
        prompt
    )

    return json.loads(result)