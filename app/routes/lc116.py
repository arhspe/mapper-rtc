from fastapi import APIRouter, HTTPException, Request
from app.models.correlation import CorrelationResponse
from app.services import loader

router = APIRouter()

@router.get("/{code}", response_model=CorrelationResponse)
def get_correlation_by_lc116(code: str, request: Request):
    path_parts = request.url.path.strip("/").split("/")
    version = path_parts[0] 
    
    result = loader.get_by_lc116(version, code)
    
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"Codigo LC 116 '{code}' nao encontrado na versao {version}"
        )
        
    return result