from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config.settings import settings
from app.core.logging import logger

from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.clients import router as clients_router
from app.routes.invoices import router as invoices_router
from app.routes.dashboard import router as dashboard_router

app = FastAPI(title="FacturePro API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"{request.method} {request.url.path} - {type(exc).__name__}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Une erreur interne est survenue."},
    )


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(clients_router)
app.include_router(invoices_router)
app.include_router(dashboard_router)


@app.get("/")
def root():
    logger.info("Health check")
    return {"message": "FacturePro API running"}
