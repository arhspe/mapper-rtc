from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/status")
def get_api_status():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": "production"
    }