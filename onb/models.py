from __future__ import annotations
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class ToolCall(BaseModel):
    """Payload sent from the Copilot to ONB.
    ``action`` is one of: next_step, save_answer, save_file, submit, get_review.
    ``data`` holds the tool‑specific fields.
    """
    action: str = Field(..., description="Tool name")
    data: Dict[str, Any] = Field(..., description="Tool‑specific parameters")

class ToolResult(BaseModel):
    """Response from ONB back to the Copilot.
    The shape varies per tool; we keep a flexible ``result`` dict.
    """
    result: Dict[str, Any] = Field(..., description="Tool‑specific output")

# Specific request/response models (optional, for clearer typing)
class NextStepRequest(BaseModel):
    review_id: str

class NextStepResult(BaseModel):
    next: str
    display: str
    required: bool = True

class SaveAnswerRequest(BaseModel):
    review_id: str
    field: str
    answer: str

class SaveFileRequest(BaseModel):
    review_id: str
    field: str
    filename: str
    content_b64: str

class SubmitRequest(BaseModel):
    review_id: str

class SubmitResult(BaseModel):
    review_id: str
    status: str
    missing: List[str]
    policy_citations: List[str]

class GetReviewRequest(BaseModel):
    review_id: str

class GetReviewResult(BaseModel):
    review_id: str
    fields: Dict[str, Optional[str]]
    verdict: Optional[Dict[str, Any]]
