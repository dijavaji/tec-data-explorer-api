from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: Optional[str] = Field(default=None, description="MongoDB document ObjectID")
    #id: Optional(str)
    name: str
    lastName: str
    address: str
    email: str
    phone: str
    password: str
