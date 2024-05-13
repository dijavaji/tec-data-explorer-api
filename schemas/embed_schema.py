from pydantic import BaseModel, Field, UUID4
from typing import Optional, List
from models.token import Token
class EmbedInput(BaseModel):
    model: str = Field(min_length=1, max_length=128)
    text: str

class EmbedOutput(BaseModel):
    id: UUID4
    embeddings: List[float]
    tokens: Token
    model: str
