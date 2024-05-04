from models.chat_model import ChatOutput, ChatInput
import uuid

class ChatService:
    def __init__(self, chat):
        self.chat = chat

    def create(self, data: ChatInput) -> ChatOutput:
        #if self.repository.chat_exists_by_name(data.name):
            #raise HTTPException(status_code=400, detail="Region already exists")
        print("ingreso servicio chat")
        myuuid = uuid.uuid4()
        chate = ChatOutput(id=myuuid, model=data.model, temperature= data.temperature, messages= data.messages, max_tokens= data.max_tokens, top_p=data.top_p, stream=data.stream)
        return chate