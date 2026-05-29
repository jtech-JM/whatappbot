from datetime import datetime
from typing import List, Literal

from pydantic import BaseModel, Field, HttpUrl, confloat


class SourceGrounding(BaseModel):
    source_url: HttpUrl
    extracted_fact: str
    metric_data: str


class CoreBreakthrough(BaseModel):
    title: str
    technical_summary: str


class ResearchBriefPayload(BaseModel):
    timestamp: datetime = Field(..., description="RFC 3339 timestamp for when the research brief was generated")
    topic: str = Field(..., description="The research topic provided by the runtime invocation")
    source_grounding: List[SourceGrounding] = Field(
        ..., description="List of grounding sources and extracted facts used by the Researcher agent"
    )
    core_breakthroughs: List[CoreBreakthrough] = Field(
        ..., description="Structured list of the top technical breakthroughs identified from the research"
    )


class ScoreMetrics(BaseModel):
    factual_alignment_score: confloat(ge=0.0, le=1.0) = Field(
        ..., description="Normalized alignment score between draft content and source grounding"
    )
    formatting_compliance: bool = Field(
        ..., description="Whether the generated content matches the required markdown and structural rules"
    )


class ContentEvaluationSchema(BaseModel):
    evaluation_status: Literal["APPROVED", "REJECTED"] = Field(
        ..., description="Final approval status from the Editor/Critic node"
    )
    score_metrics: ScoreMetrics = Field(..., description="Quantitative evaluation metrics for the draft")
    feedback_logs: str = Field(
        default="",
        description="Actionable revision guidance when the draft is rejected, empty when approved",
    )


__all__ = [
    "SourceGrounding",
    "CoreBreakthrough",
    "ResearchBriefPayload",
    "ScoreMetrics",
    "ContentEvaluationSchema",
]
