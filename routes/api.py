from fastapi import APIRouter
from routes import chat_routes, user_routes, embed_routes

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(chat_routes.router)
router.include_router(user_routes.router)
router.include_router(embed_routes.router)
#app.include_router(jwt_auth_users.router)
#app.mount("/static", StaticFiles(directory="static"), name="static")