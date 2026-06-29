import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager

from app.status import router as status_router
from app.services.loader import initialize_search_service

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_search_service()
    yield

app = FastAPI(
    title="Mapper RTC",
    version="2.0.0",
    description="Serviço de consulta e mapeamento cruzado entre a LC 116/2003 e os novos indexadores de IBS/CBS da Reforma Tributária.",
    lifespan=lifespan
)

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

app.include_router(status_router, tags=["Global"])

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/processed"))

if os.path.exists(DATA_DIR):

    versions = [d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d)) and d.startswith('v')]
    
    from app.routes.lc116 import router as lc116_router

    for version in versions:
        app.include_router(
            lc116_router, 
            prefix=f"/{version}/lc116", 
            tags=[f"LC 116 ({version})"]
        )
else:
    print(f"[warning] diretorio de dados nao encontrado em: {DATA_DIR}")