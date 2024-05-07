from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder
from models.user import User
from schemas.user_schema import UserInput, UserOutput
from typing import List, Optional, Type
from pydantic import UUID4
from schemas.user_schema import user_schema, users_schema
from bson import ObjectId

class UserRepository:
    def __init__(self, session: MongoClient):
        self.session = session
    def create(self, user : UserInput) -> UserOutput:
        #user_dic = dict(user)
        user_dic = jsonable_encoder(User(**user.model_dump(exclude_none=True)))
        del user_dic["id"]
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

    def update(self, id:str, data: UserInput) -> UserInput:
        user = jsonable_encoder(User(**data.model_dump(exclude_none=True)))
        del user["id"]
        print("actualizo user", user)
        try:
           update_result = self.session.users.find_one_and_replace({"_id": ObjectId(id)}, user)
           #update_result = self.session.database["users"].update_one({"_id": ObjectId(id)}, {"$set": user})
           #print(update_result)
           return UserInput(**search_user_by_field("_id",id))
        except:
            print({"error": "No se a encontrado el usuario"})
            return data
        #return search_user("_id", ObjectId(user.id))
        #return data

    def delete(self,id):
        return self.session.users.find_one_and_delete({"_id": ObjectId(id)})