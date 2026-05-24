from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import router as auth_router

from app.routes.users import router as users_router

from app.routes.clients import router as clients_router

from app.routes.invoices import router as invoices_router

from app.routes.dashboard import router as dashboard_router

app = FastAPI(title="FacturePro API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(clients_router)
app.include_router(invoices_router)
app.include_router(dashboard_router)


@app.get("/")
def root():
    return {"message": "FacturePro API running"}
