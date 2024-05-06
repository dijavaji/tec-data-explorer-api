from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder
from models.user import User
from schemas.user_schema import UserInput, UserOutput
from typing import List, Optional, Type
from pydantic import UUID4
from schemas.user_schema import user_schema, users_schema
class UserRepository:
    def __init__(self, session: MongoClient):
        self.session = session
    def create(self, user : UserInput) -> UserOutput:
        #user_dic = dict(user)
        #del user_dic["id"]
        user_dic = jsonable_encoder(User(**user.model_dump(exclude_none=True)))
        new_user = self.session.users.insert_one(user_dic)
        created_user = user_schema(self.session.users.find_one({"_id": new_user.inserted_id}))
        return UserOutput(**created_user)

    def get_all(self) -> List[Optional[UserOutput]]:
        users = users_schema(self.session.users.find())
        return [UserOutput(**user) for user in users]

    def search_user_by_field(self, field: str, key) -> UserOutput:
        try:
            print("ingreso a buscar usuario by field")
            user = self.session.users.find_one({field: key})
            userout = UserOutput(**user_schema(user))
            print(userout)
            return userout
        except:
            return {"error": "No se a encontrado el usuario"}