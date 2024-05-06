import uuid
from pydantic import BaseModel, UUID4, Field
from typing import Optional
#from .person_schema import PersonOutput

def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "name": user["name"],
            "lastName": user["lastName"],
            "address": user["address"],
            "email": user["email"],
            "phone": user["phone"],
            "password": user["password"]
    }


def users_schema(users) -> list:
    return [user_schema(user) for user in users]

class UserInput(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    lastName: str
    address: str
    email: str
    phone: str
    password: str

class UserOutput(BaseModel):
    id: Optional[str] = Field(default_factory=uuid.uuid4, description="MongoDB document ObjectID")
    name: str
    lastName: str
    address: str
    email: str
    phone: str
    password: str
    #person: PersonOutput
