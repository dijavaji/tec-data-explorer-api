from fastapi import APIRouter, HTTPException, status
from schemas.embed_schema import EmbedInput, EmbedOutput
from service.embed_service import embed_service

router = APIRouter(prefix="/embed",
                   tags=["text embeddings"],
                   responses={status.HTTP_404_NOT_FOUND :{"message":"No encontrado"}})

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=EmbedOutput,
             summary="create_embedding",
             description="Utilizado para convertir texto enbedding"
             )
async def create_embedding(data : EmbedInput):
    return embed_service.create_embed(data)

