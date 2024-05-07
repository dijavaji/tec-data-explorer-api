from repository.tokenize_repository import tokenize_repository
from schemas.tokenize_schema import TokenizeInput, TokenizeOutput
class TokenizeService:
    def create_tokenize(self, data: TokenizeInput) -> TokenizeOutput:
        return tokenize_repository.create_tokenize(data)


tokenize_service = TokenizeService()