#pip install langchain sentence_transformers
#pip install -U langchain-community
import uuid
from models.token import Token
from schemas.embed_schema import EmbedInput, EmbedOutput
#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from utils.dataExplorer_constant import APP_MULTI_PROCESS

class EmbedRepository:
    def __init__(self):
        self.users = []

    def create_embed(self, data: EmbedInput) -> EmbedOutput:
        #self.users.append(user)
        if data.model is None or data.model == " ":
            model = "sentence-transformers/all-mpnet-base-v2"
        else:
            model = data.model
        model_name = model
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': False}
       # multi_process = APP_MULTI_PROCESS
        #embeddings = HuggingFaceEmbeddings() # por defecto utilza el modelo all-mpnet-base-v2
        hf = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
        query_result = hf.embed_query(data.text)
        print(query_result[:3])
        #doc_result = embeddings.embed_documents([text])
        myuuid = uuid.uuid4()
        token = Token(input_tokens=0, output_tokens=0)
        return EmbedOutput(id = myuuid, embeddings= query_result, model=model, tokens=token)

embed_repository = EmbedRepository()
