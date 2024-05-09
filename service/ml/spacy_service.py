import spacy
from utils.cleanerMl_util import CleanerMlUtil
from schemas.chat_schemas import ChatOutput, ChatInput
from schemas.message_schema import convert_dict
from models.message_model import Message
import uuid

class SpacyService:

    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")

    def create_completions(self, data: ChatInput) -> ChatOutput:
        myuuid = uuid.uuid4()
        respuesta = self.__obtener_respuesta(data.messages, data.top_p)
        print("respuesta spacy",respuesta.content)
        response_messages=[respuesta]
        chate = ChatOutput(id=myuuid, model=data.model, temperature= data.temperature, messages= response_messages, max_tokens= data.max_tokens, top_p=data.top_p, stream=data.stream)
        return chate

    def __obtener_respuesta(self, messages, top_p) -> Message:
        # printing initial list of dictionary
        print("initial_list", str(messages))
        # code to filter list where role is system or assistant
        question_answers = list(filter(lambda x: x.role == "system" or x.role == "assistant", messages))

        user_messages = list(filter(lambda x: x.role == "user", messages))
        #print("resultant_list", str(user_messages))
        user_message = user_messages.pop(0)     #tomo pregunta del usuario
        texto = user_message.content
        cleaner = CleanerMlUtil()
        texto = cleaner.clean_words(texto)
        doc = self.nlp(texto)
        respuestas = convert_dict(question_answers)
        # print(respuestas)
        for pregunta in respuestas:
            if self.nlp(pregunta).similarity(doc) > top_p:
                msg_out = Message(role="assistant", content=respuestas[pregunta])
                return msg_out
        return Message(role="assistant", content="no existe en corpus")

spacy_service = SpacyService()