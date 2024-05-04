#source .venv/bin/activate
#inicio fastapi
#pip install fastapi
#pip install "uvicorn[standard]"
#pip install pymongo
#pip install -r  requirements.txt

#Iniciar el server:  uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import chat_routes, jwt_auth_users, users_db

app = FastAPI()

#routes
app.include_router(chat_routes.router)
app.include_router(jwt_auth_users.router)
#app.include_router(users_db.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

#url local http://127.0.0.1:8000/
#http://localhost:8000/docs
#http://localhost:8000/redoc
@app.get("/messages")
async def root():
	return "Now this finally works out. Welcome"



