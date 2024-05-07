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


@router.get("/", status_code=200, response_model=UserOutput) #query
async def user(id:str, session: MongoClient = Depends(get_db)):
    _service = UserService(session)
    return _service.getUser(id)  # search_user("_id", ObjectId(id))

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOutput)
async def createUser(data : UserInput, session: MongoClient = Depends(get_db)):
    _service = UserService(session)
    print("ingreso a guardar")
    return _service.create(data)

@router.put("/{id}",response_description="Update a user", status_code=200,  response_model=UserInput)
async def updateUser(id:str, data : UserInput, session: MongoClient = Depends(get_db)):
    _service = UserService(session)
    print("ingreso a actualizar usuario")
    return _service.update(id, data)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteUser(id: str, session: MongoClient = Depends(get_db)):
    _service = UserService(session)
    print("ingreso a eliminar usuario")
    _service.delete(id)






