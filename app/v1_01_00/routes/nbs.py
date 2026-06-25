from fastapi import APIRouter, HTTPException
from app.v1_01_00.models.correlation import CorrelationResponse
from app.v1_01_00.services import search_service

router = APIRouter()

@router.get("/{code}", response_model=CorrelationResponse)
def get_correlation_by_nbs(code: str):
    
    result = search_service.get_by_nbs(code)
    
    if not result:
        raise HTTPException(
            status_code=404, 
            detail=f"codigo NBS '{code}' nao encontrado na versao v1_01_00"
        )
        
    return result