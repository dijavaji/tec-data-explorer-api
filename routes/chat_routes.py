from fastapi import APIRouter, HTTPException, status
from models.chat_model import ChatOutput, ChatInput
from service.chat_service import ChatService

router = APIRouter(prefix="/api/v1/chat",
                   tags=["chat"],
                   responses={404:{"message":"No encontrado"}})

@router.post("/completions", status_code=status.HTTP_201_CREATED, response_model=ChatOutput)
async def createCompletions(chatData : ChatInput):
    _service = ChatService(chatData)
    return _service.create(chatData)

