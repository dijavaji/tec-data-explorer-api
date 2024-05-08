from pydantic import BaseModel, UUID4, Field
from typing import Optional, List
from models.message_model import Message
from utils.cleanerMl_util import CleanerMlUtil
from fastapi.encoders import jsonable_encoder
class ChatInput(BaseModel):
    model: str = Field(min_length=1, max_length=120)
    temperature: float
    messages: List[Message]
    max_tokens: int
    top_p: float
    stream: bool


class ChatOutput(BaseModel):
    id: UUID4
    model: str
    temperature: float
    messages: List[Message]
    max_tokens: int
    top_p: float
    stream: bool
