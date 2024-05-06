from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from pymongo import MongoClient
from models.user import User
from models.db.clientDb import get_db
from service.user_service import UserService
from schemas.user_schema import user_schema, users_schema, UserOutput, UserInput
from bson import ObjectId

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={status.HTTP_404_NOT_FOUND:{"message":"No encontrado"}})

users_list =[]

@router.get("/list", status_code=200, response_model=List[UserOutput])
async def findUsers(session: MongoClient = Depends(get_db)):
    _service = UserService(session)
    return _service.get_all() #users_schema(db.users.find())

#path
@router.get("/{id}",  status_code=200, response_description="Get a single user by id", response_model=UserOutput)
async def getUser(id:str, session: MongoClient = Depends(get_db)):
    _service = UserService(session)
    return _service.getUser(id)  #search_user("_id", ObjectId(id))


@router.get("/") #query
async def user(id:str):
    _service = UserService(session)
    return _service.getUser(id)  # search_user("_id", ObjectId(id))

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOutput)
async def createUser(data : UserInput, session: MongoClient = Depends(get_db)):
    _service = UserService(session)
    print("ingreso a guardar")
    return _service.create(data)

@router.put("/", response_model=User)
async def updateUser(user : User):
    user_dic = dict(user)
    del user_dic["id"]
    try:
        db.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dic)
    except:
        return {"error": "No se a encontrado el usuario"}
    return search_user("_id", ObjectId(user.id))

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteUser(id: str):
    found = db.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se a eliminado el usuario"}



def search_user(field:str, key):
    try:
        db = get_db()
        print("ingreso a buscar usuario", db)
        user = db.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "No se a encontrado el usuario"}



