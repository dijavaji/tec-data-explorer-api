#pip install langchain sentence_transformers
#pip install -U langchain-community
from models.tokenize import Tokenize
from schemas.tokenize_schema import TokenizeInput, TokenizeOutput
from langchain_community.embeddings import HuggingFaceEmbeddings

class TokenizeRepository:
    def __init__(self):
        self.users = []

    def create_tokenize(self, data: TokenizeInput) -> TokenizeOutput:
        #self.users.append(user)
        model_name = "sentence-transformers/"+data.model
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': False}
        #embeddings = HuggingFaceEmbeddings() # por defecto utilza el modelo all-mpnet-base-v2
        hf = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
        query_result = hf.embed_query(data.text)
        print(query_result[:3])
        #doc_result = embeddings.embed_documents([text])
        return TokenizeOutput(tokens= query_result, token_strings= ["palabras"])

tokenize_repository = TokenizeRepository()