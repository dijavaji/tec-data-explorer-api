from fastapi import APIRouter, HTTPException, status
from schemas.chat_schemas import ChatOutput, ChatInput
from service.chat_service import ChatService

# description="Microservicio de inteligencia artificial de alto rendimiento, confiable e inteligente creada por Technoloqie.",
router = APIRouter(prefix="/chat",
                   tags=["Chat API"],
                   responses={status.HTTP_404_NOT_FOUND :{"message":"No encontrado"}})

@router.post("/completions", status_code=status.HTTP_201_CREATED, response_model=ChatOutput,
             summary="create_completions",
             description="Env&#237;e una lista estructurada de mensajes de entrada con contenido de texto, y el modelo generar&#225; el pr&#243;ximo mensaje en la conversaci&#243;n."
             )
async def create_completions(chatData : ChatInput):
    _service = ChatService(chatData)
    return _service.create(chatData)

