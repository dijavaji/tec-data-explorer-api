from fastapi import APIRouter, HTTPException, status
from schemas.tokenize_schema import TokenizeInput, TokenizeOutput
from service.tokenize_service import tokenize_service

router = APIRouter(prefix="/tokenize",
                   tags=["tokenize"],
                   responses={status.HTTP_404_NOT_FOUND :{"message":"No encontrado"}})

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TokenizeOutput)
async def create_tokenizes(data : TokenizeInput):
    return tokenize_service.create_tokenize(data)

