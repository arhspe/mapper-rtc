import logging
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.exceptions import RequestValidationError
from contextlib import asynccontextmanager

from app.routes.status import router as status_router
from app.routes.lc116 import router as lc116_router
from app.services.loader import initialize_search_service

logger = logging.getLogger("uvicorn.error")

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_search_service()
    yield

app = FastAPI(
    title="Mapper RTC",
    version="1.0.0",
    description="Serviço de consulta e mapeamento cruzado entre a LC 116/2003 e os novos indexadores da Reforma Tributária.",
    lifespan=lifespan
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    erros = []
    for error in exc.errors():
        erros.append({
            "field": " -> ".join([str(loc) for loc in error["loc"] if loc != "body"]),
            "message": error["msg"]
        })

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": {
                "code": "VALIDATION_ERROR",
                "message": "Parametros enviados na requisicao sao invalidos.",
                "errors": erros
            }
        }
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Erro nao tratado capturado: {exc}", exc_info=True)
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "Erro interno inesperado no servidor."
            }
        }
    )

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

app.include_router(status_router, tags=["Status"])
app.include_router(
    lc116_router,
    prefix="/{version}/lc116",
    tags=["Correlações LC 116"]
)