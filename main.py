#source .venv/bin/activate
#inicio fastapi
#pip install fastapi
#pip install "uvicorn[standard]"
#pip install pymongo

#Iniciar el server:  uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import products, users, jwt_auth_users, users_db

app = FastAPI()

#routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

#url local http://127.0.0.1:8000/
@app.get("/")
async def root():
	return "Hola mundo fastapi"
	
@app.get("/url")
async def url():
        return {"url":"https://technoloqie.website"}


