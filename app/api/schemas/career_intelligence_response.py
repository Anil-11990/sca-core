"""
API Response Schema for Career Intelligence.
"""

from pydantic import BaseModel, Field


class CareerInsightSchema(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    category: str = Field(...)


class MarketSignalSchema(BaseModel):
    skill: str = Field(...)
    demand_level: str = Field(...)
    trend: str = Field(...)
    source: str = Field(...)


class RecommendationSchema(BaseModel):
    action: str = Field(...)
    reason: str = Field(...)
    priority: str = Field(...)


class CareerIntelligenceResponse(BaseModel):
    insight: CareerInsightSchema
    market_signals: list[MarketSignalSchema]
    recommendations: list[RecommendationSchema]