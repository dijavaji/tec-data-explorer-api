from pydantic import BaseModel, Field
from typing import Optional, List
class Tokenize(BaseModel):
    id: Optional[str] = Field(default=None, description="MongoDB document ObjectID")
    tokens: List[float]
    token_strings: List[str]