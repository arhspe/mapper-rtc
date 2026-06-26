from fastapi import FastAPI
from fastapi.responses import RedirectResponse 
from contextlib import asynccontextmanager
from app.status import router as status_router
from app.v1_01_00.routes import lc116, nbs
from app.v1_01_00.services.search_service import initialize_search_service

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_search_service()
    yield

app = FastAPI(
    title="Mapper RTC",
    description="Serviço de consulta e mapeamento cruzado entre a LC 116/2003 e os novos indexadores de IBS/CBS da Reforma Tributária.",
    lifespan=lifespan
)

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

app.include_router(status_router, tags=["Global"])
app.include_router(lc116.router, prefix="/v1_01_00/lc116", tags=["LC 116 (v1.01.00)"])
app.include_router(nbs.router, prefix="/v1_01_00/nbs", tags=["NBS (v1.01.00)"])
