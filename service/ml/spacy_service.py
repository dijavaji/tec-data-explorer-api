import spacy
from utils.cleanerMl_util import CleanerMlUtil
from schemas.chat_schemas import ChatOutput, ChatInput
from schemas.message_schema import convert_dict
import uuid

class SpacyService:

    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")

    def create_completions(self, data: ChatInput) -> ChatOutput:
        #if self.repository.chat_exists_by_name(data.name):
            #raise HTTPException(status_code=400, detail="Region already exists")
        print("ingreso servicio spacy")
        myuuid = uuid.uuid4()
        respuesta = self.obtener_respuesta(data.messages)
        print("respuesta spacy",respuesta)
        chate = ChatOutput(id=myuuid, model=data.model, temperature= data.temperature, messages= data.messages, max_tokens= data.max_tokens, top_p=data.top_p, stream=data.stream)
        return chate

    def obtener_respuesta(self, messages):
        texto="Hola como estas"
        print(messages)
        cleaner = CleanerMlUtil()
        texto = cleaner.clean_words(texto)
        doc = self.nlp(texto)
        respuestas = convert_dict(messages)
        # print(respuestas)
        for pregunta in respuestas:
            if self.nlp(pregunta).similarity(doc) > 0.7:
                return respuestas[pregunta]
        return "Lo siento, no entendí la pregunta."

spacy_service = SpacyService()