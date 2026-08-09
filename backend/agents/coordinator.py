# backend/agents/coordinator.py

import asyncio

from agents.financial_agent import analyze_financials
from agents.news_agent import analyze_news
from agents.industry_agent import analyze_industry
from agents.risk_agent import analyze_risks
from agents.competitor_agent import analyze_competitors
from agents.decision_agent import generate_recommendation
from services.memo_builder import build_investment_prompt
from services.openai_client import ask_llm
from services.report_storage import (save_report, save_decision, create_timestamp)
from services.market_data import get_company_data
from services.metrics import extract_key_metrics

def calculate_average_score(decision):
    return (
        decision["financial_score"]
        + decision["industry_score"]
        + decision["competitive_score"]
        + decision["safety_score"]
    ) / 4


def average_score_to_rating(avg_score):
    if avg_score >= 8:
        return "BUY"
    if avg_score >= 6:
        return "WATCHLIST"
    return "SELL"


def average_score_to_confidence(avg_score):
    return round(avg_score)


async def run_research(symbol: str):
    from datetime import datetime
    async def run_research(symbol: str):
        print(f"[{datetime.now()}] run_research called for {symbol}")
    
    (
        financials,
        news,
        industry,
        risks,
        competitors
    ) = await asyncio.gather(
        analyze_financials(symbol),
        analyze_news(symbol),
        analyze_industry(symbol),
        analyze_risks(symbol),
        analyze_competitors(symbol)
    )

    prompt = build_investment_prompt(
        company=symbol,
        financials=financials,
        news=news,
        industry=industry,
        risks=risks,
        competitors=competitors
    )

    investment_memo = await asyncio.to_thread(ask_llm, prompt)
    timestamp = create_timestamp()
    report_path = save_report(symbol, investment_memo, timestamp)
    company_data = await asyncio.to_thread(get_company_data, symbol)
    key_metrics = extract_key_metrics(company_data)

    decision = await generate_recommendation(
        symbol,
        financials,
        news,
        industry,
        risks,
        competitors
    )
    
    average_score = calculate_average_score(decision)
    
    final_decision = {
        "company": symbol,
        "rating": average_score_to_rating(average_score),
        "confidence": average_score_to_confidence(average_score),
        "financial_score": decision["financial_score"],
        "industry_score": decision["industry_score"],
        "competitive_score": decision["competitive_score"],
        "safety_score": decision["safety_score"],
        "thesis": decision["thesis"],
        "key_metrics": key_metrics,
        "strengths": decision["strengths"],
        "risks": decision["risks"],
        "upgrade_catalyst": decision["upgrade_catalyst"],
        "downgrade_catalyst": decision["downgrade_catalyst"],
        "report_file": report_path
    }

    save_decision(symbol, final_decision, timestamp)

    return final_decision