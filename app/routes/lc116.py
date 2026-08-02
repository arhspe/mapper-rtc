import re
from fastapi import APIRouter, HTTPException, status
from app.models.correlation import CorrelationResponse
from app.services import loader

router = APIRouter()

CODE_PATTERN = r"^\d{2}\.\d{2}$"

@router.get("/{code}", response_model=CorrelationResponse)
def get_correlation_by_lc116(version: str, code: str):

    if not re.match(CODE_PATTERN, code):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "code": "INVALID_CODE_FORMAT",
                "message": f"O codigo '{code}' e invalido. Ele deve seguir o padrao 'XX.XX' (ex: '01.01').",
                "item_searched": code
            }
        )

    if not loader.version_exists(version):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "code": "VERSION_NOT_FOUND",
                "message": f"A versao '{version}' nao foi encontrada ou nao existe.",
                "available_versions": loader.get_available_versions()
            }
        )
    
    result = loader.get_by_lc116(version, code)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "code": "LC116_ITEM_NOT_FOUND",
                "message": f"O item '{code}' nao foi encontrado na versao '{version}'.",
                "version_searched": version,
                "item_searched": code
            }
        )

    return result