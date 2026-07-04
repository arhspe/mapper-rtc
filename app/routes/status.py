import os
from datetime import datetime, timezone
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

START_TIME = datetime.now(timezone.utc)

class AppStatus(BaseModel):
    name: str
    api_version: str
    environment: str

class SystemStatus(BaseModel):
    timestamp: str
    uptime: str

class StatusResponse(BaseModel):
    status: str
    app: AppStatus
    system: SystemStatus


@router.get("/status", response_model=StatusResponse)
def get_api_status():
    now = datetime.now(timezone.utc)
    uptime = now - START_TIME  

    return {
        "status": "healthy",
        "app": {
            "name": "Mapper RTC",
            "api_version": "1.0.0",  
            "environment": os.getenv("ENV", "development"),
        },
        "system": {
            "timestamp": now.isoformat(),
            "uptime": str(uptime).split(".")[0]
        }
    }