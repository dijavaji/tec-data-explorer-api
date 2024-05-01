from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.clientDb import db
from db.schemas.user import user_schema, users_schema
from bson import ObjectId

router = APIRouter(prefix="/user",
                   tags=["users"],
                   responses={status.HTTP_404_NOT_FOUND:{"message":"No encontrado"}})

users_list =[]

@router.get("/", response_model=list[User])
async def findUsers():
    return users_schema(db.users.find())

@router.get("/{id}") #path
async def getUser(id:str):
    return search_user("_id", ObjectId(id))


@router.get("/") #query
async def user(id:str):
    return search_user("_id", ObjectId(id))

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
async def createUser(user : User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe") # return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)
    user_dic = dict(user)
    del user_dic["id"]
    id = db.users.insert_one(user_dic).inserted_id
    new_user = user_schema(db.users.find_one({"_id": id}))
    return User(**new_user)

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
        user = db.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "No se a encontrado el usuario"}



