# Iniciar el server
# uvicorn main:app --reload
#documentacion con swagger http://127.0.0.1:8000/docs#
#documentacion con redocly http://127.0.0.1:8000/redoc

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

#entidad User
class User(BaseModel):
    id:int
    name: str
    surname: str
    url: str
    age: int

users_list =[User(id=1, name="Pepito", surname="Hardvard", url="https://technoloqie.website", age=27),
        User(id=2, name="Mad", surname="Technoloqie", url="https://mad.net", age=27),
        User(id=3, name="Ada", surname="lovelace", url="https://lovelace.net", age=27)]

@router.get("/usersjson")
async def usersjson():
    return [{"name":"Pepito", "surname":"Hardvard", "url":"https://technoloqie.website", "age":27}]

@router.get("/users")
async def users():
    return users_list

#Path   parametros que van fijos mandatorios http://127.0.0.1:8000/users/1
@router.get("/users/{id}")
async def user(id:int):
    return search_user(id)

#Query
# parametros que no son necesarios para hacer la peticion  http://127.0.0.1:8000/users/?id=3&otro=algo
#ejm la paginacion
@router.get("/users/")
async def user(id:int):
    return search_user(id)

@router.post("/users/", status_code=201, response_model=User)
async def user(user : User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe") # return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)

@router.put("/users/")
async def user(user : User):
    found = False
    for index, saver_user in enumerate(users_list):
        if saver_user.id == user.id:
            users_list[index] =user
            found = True
    if not found:
        return {"error": "No se a encontrado el usuario"}

@router.delete("/users/{id}")
async def deleteUser(id:int):
    found = False
    for index, saver_user in enumerate(users_list):
        if saver_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se a eliminado el usuario"}


def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se a encontrado el usuario"}



