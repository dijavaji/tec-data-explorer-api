from fastapi import APIRouter, HTTPException, status
from schemas.chat_schemas import ChatOutput, ChatInput
from service.chat_service import ChatService

router = APIRouter(prefix="/chat",
                   tags=["chat"],
                   responses={status.HTTP_404_NOT_FOUND :{"message":"No encontrado"}})

@router.post("/completions", status_code=status.HTTP_201_CREATED, response_model=ChatOutput)
async def create_completions(chatData : ChatInput):
    _service = ChatService(chatData)
    return _service.create(chatData)

