from pydantic import BaseModel, Field
from typing import Optional, List
class TokenizeInput(BaseModel):
    model: str = Field(min_length=1, max_length=32)
    text: str

class TokenizeOutput(BaseModel):
    tokens: List[float]
    token_strings: List[str]
