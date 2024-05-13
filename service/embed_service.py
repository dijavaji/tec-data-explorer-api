from repository.embed_repository import embed_repository
from schemas.embed_schema import EmbedInput, EmbedOutput
class EmbedService:
    def create_embed(self, data: EmbedInput) -> EmbedOutput:
        return embed_repository.create_embed(data)


embed_service = EmbedService()