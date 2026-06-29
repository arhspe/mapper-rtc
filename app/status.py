from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter()

@router.get("/status")
def get_api_status():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "environment": "production"
    }