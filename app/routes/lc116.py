from fastapi import APIRouter, HTTPException
from app.models.correlation import CorrelationResponse
from app.services import loader

router = APIRouter()

@router.get("/{code}", response_model=CorrelationResponse)
def get_correlation_by_lc116(version: str, code: str):
    result = loader.get_by_lc116(version, code)
    
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"codigo '{code}' nao encontrado na versao '{version}'"
        )
        
    return result