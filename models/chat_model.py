from pydantic import BaseModel, UUID4, Field
from typing import Optional
from models.message_model import Message

class Chat(BaseModel):
    #id: Optional[str] = Field(default=None, description="MongoDB document ObjectID")
    #id: Optional(str)
    model: str
    temperature: float
    messages: Message
    max_tokens: int
    top_p: float
    stream: bool

class ChatInput(BaseModel):
    model: str = Field(min_length=1, max_length=120)
    temperature: float
    messages: Message
    max_tokens: int
    top_p: float
    stream: bool


class ChatOutput(BaseModel):
    id: UUID4
    model: str
    temperature: float
    messages: Message
    max_tokens: int
    top_p: float
    stream: bool