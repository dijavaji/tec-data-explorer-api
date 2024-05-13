from pydantic import BaseModel, Field
from typing import Optional, List
class Token(BaseModel):
    #id: Optional[str] = Field(default=None, description="MongoDB document ObjectID")
    input_tokens: int
    output_tokens: int
