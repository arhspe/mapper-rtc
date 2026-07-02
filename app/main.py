import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager

from app.status import router as status_router
from app.routes.lc116 import router as lc116_router
from app.services.loader import initialize_search_service

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_search_service()
    yield

app = FastAPI(
    title="Mapper RTC",
    version="3.0.0",
    description="Serviço de consulta e mapeamento cruzado entre a LC 116/2003 e os novos indexadores de IBS/CBS.",
    lifespan=lifespan
)

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

app.include_router(status_router, tags=["Status"])

app.include_router(
    lc116_router,
    prefix="/{version}/lc116",
    tags=["Correlações Fiscais"]
)