from pymongo import MongoClient
from typing import List, Optional

from fastapi import HTTPException, status
from pydantic import UUID4
from repository.user_repository import UserRepository
from schemas.user_schema import UserInput, UserOutput
from bson import ObjectId


class UserService:
    def __init__(self, session: MongoClient):
        self.repository = UserRepository(session)

    def create(self, data: UserInput) -> UserOutput:
        if type(self.repository.search_user_by_field("email", data.email)) == UserOutput:
            raise HTTPException(status_code=400, detail="Usuario ya existe")
        return self.repository.create(data)

    def get_all(self) -> List[Optional[UserOutput]]:
        return self.repository.get_all()

    def getUser(self, id:str) -> UserOutput:
        return self.repository.search_user_by_field("_id", ObjectId(id))

    def update(self, id:str, data: UserInput) -> UserInput:
        user = self.repository.search_user_by_field("_id", ObjectId(id))
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")
        return self.repository.update(id, data)

    def delete(self, id:str):
        found = self.repository.delete(id)
        print("eliminado",found)
        if not found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")

