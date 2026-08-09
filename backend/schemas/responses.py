# backend/schema/responses.py

from pydantic import BaseModel


class ResearchResponse(BaseModel):
    company: str
    rating: str
    confidence: int
    financial_score: int
    industry_score: int
    competitive_score: int
    safety_score: int
    thesis: str
    key_metrics: dict
    strengths: list[str]
    risks: list[str]
    upgrade_catalyst: str
    downgrade_catalyst: str
    report_file: str