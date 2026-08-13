from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, gatepass, visitor
from app.core.database import Base, engine
from app.models import models


app = FastAPI(title="Visitor Entry & Gate Pass Management System")

Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
