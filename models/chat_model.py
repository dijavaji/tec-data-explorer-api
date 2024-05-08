from pydantic import BaseModel, UUID4, Field
from typing import Optional, List
from models.message_model import Message

class Chat(BaseModel):
    #id: Optional[str] = Field(default=None, description="MongoDB document ObjectID")
    #id: Optional(str)
    model: str
    temperature: float
    messages: List[Message]
    max_tokens: int
    top_p: float
    stream: bool
