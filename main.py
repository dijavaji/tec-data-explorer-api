#source .venv/bin/activate
#inicio fastapi
#pip install fastapi
#pip install "uvicorn[standard]"
#pip install pymongo
#pip install -r  requirements.txt

#Iniciar el server:  uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.api import router
from fastapi.middleware.cors import CORSMiddleware
#from routes import chat_routes, jwt_auth_users, users_db

app = FastAPI(
	debug=True,
    title="DataExplorer",
)

origins = [
  	"http://localhost",
    "http://127.0.0.1:8080",
	"http://127.0.0.1:8085",
	"http://0.0.0.0",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#@app.on_event("startup")
#def on_startup() -> None:

	#print("Connected to the MongoDB database!")

#routes
app.include_router(router)
#cambio a archivo api.py
#app.include_router(chat_routes.router)
#app.include_router(jwt_auth_users.router)
#app.include_router(users_db.router)
#app.mount("/static", StaticFiles(directory="static"), name="static")

#url local http://127.0.0.1:8000/
#http://localhost:8000/docs
#http://localhost:8000/redoc
@app.get("/messages")
async def messages():
	return "Now this finally works out. Welcome"



