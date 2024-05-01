from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM="HS256"
ACCESS_TOKEN_DURATION= 1    #indica duracion en min
# openssl rand -hex 32
SECRET_KEY = "18af092e84df55ddce4af4df4abce0390ed514bf25b7e75dc35b7b0261782f88"

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="/login")

crypt= CryptContext(schemes=["bcrypt"])

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
        "password":"$2a$12$UoHFvc8PY1adq3x8hZGJfeVETdWnhLxDWtqh3y8cefPRbsW0vxaRG"
    },
"user2":{
        "username":"user2",
        "fullName":"Pepito Hardvard 2",
        "email":"pHardvard2@mail.pbx",
        "disabled":True,
        "password":"$2a$12$UoHFvc8PY1adq3x8hZGJfeVETdWnhLxDWtqh3y8cefPRbsW0vxaRG"
    }
}

@router.post("/login")
async def login(form : OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = serch_user_db(form.username)
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    access_token ={
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION) ,
    }
    ##mas seguro enviar la semilla al jwt SECRET_KEY
    return {"access_token": jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM) , "token_type":"bearer"}


def serch_user_db(userName: str):
    if userName in users_db:
        return UserDB(**users_db[userName])

def search_user(userName: str):
    if userName in users_db:
        return User(**users_db[userName])

async def auth_user(token:str= Depends(oauth2)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticacion invalidas",
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        username = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception
    return search_user(username)

async def current_user(user: User =Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    return user

@router.get("/users/me")
async def me(user:User= Depends(current_user)):
    return user