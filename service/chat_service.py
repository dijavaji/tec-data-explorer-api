from schemas.chat_schemas import ChatOutput, ChatInput
from service.ml.spacy_service import spacy_service
from repository.chat_repository import chat_repository
import uuid

class ChatService:
    def __init__(self, chat):
        self.chat = chat

    def create(self, data: ChatInput) -> ChatOutput:
        #if self.repository.chat_exists_by_name(data.name):
            #raise HTTPException(status_code=400, detail="Region already exists")
        print("ingreso servicio chat")
        if(data.model == 'spacy'):
            chate = spacy_service.create_completions(data)
        else:
            chate = chat_repository.create_completions(data)
        return chate