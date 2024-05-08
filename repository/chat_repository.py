from typing import Optional, List
from models.message_model import Message
from schemas.chat_schemas import ChatOutput, ChatInput
class ChatRepository:
    def __init__(self):
        self.messages = List[Message]

    def create_completions(self, data: ChatInput) -> ChatOutput:
        myuuid = uuid.uuid4()
        return ChatOutput(id=myuuid, model=data.model, temperature=data.temperature, messages=data.messages,
                           max_tokens=data.max_tokens, top_p=data.top_p, stream=data.stream)


chat_repository = ChatRepository()