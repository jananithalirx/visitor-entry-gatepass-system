
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, visitor, gatepass
from app.core.database import Base, engine
from app.models import models  # noqa: F401 - import so tables register on Base.metadata

app = FastAPI(title="Visitor Entry & Gate Pass Management System")

# Create all tables on startup (fine for dev; use Alembic migrations for production)
Base.metadata.create_all(bind=engine)

# CORS - allow frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this to your frontend URL before Review-II
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(visitor.router, prefix="/api/visitors", tags=["Visitors"])
app.include_router(gatepass.router, prefix="/api/gatepass", tags=["GatePass"])


@app.get("/api/health")
def health_check():
    return {"status": "OK"}
