from pydantic import BaseModel, Field
from typing import Optional

class Message(BaseModel):
    #id: Optional[str] = Field(default=None, description="MongoDB document ObjectID")
    #id: Optional(str)
    role: str
    content: str
