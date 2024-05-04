from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

#autenticacion
oauth2 = OAuth2PasswordBearer(tokenUrl="/login")

class User(BaseModel):
    username: str
    fullName: str
    email: str
    disabled: bool

class UserDB(User):
    password:str

users_db = {
    "admin":{
        "username":"admin",
        "fullName":"Pepito Hardvard",
        "email":"pHardvard@mail.pbx",
        "disabled":False,
        "password":"123456"
    },
"user2":{
        "username":"user2",
        "fullName":"Pepito Hardvard 2",
        "email":"pHardvard2@mail.pbx",
        "disabled":True,
        "password":"123456"
    }
}

def serch_user_db(userName: str):
    if userName in users_db:
        return UserDB(**users_db[userName])

def serch_user(userName: str):
    if userName in users_db:
        return User(**users_db[userName])

@app.post("/login")
async def login(form : OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = serch_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    return {"access_token": user.username, "token_type":"bearer"}



async def current_user(token: str =Depends(oauth2)):
    user= serch_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticacion invalidas",
                            headers={"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo",
                            )
    return user

@app.get("/users/me")
async def me(user:User= Depends(current_user)):
    return user
