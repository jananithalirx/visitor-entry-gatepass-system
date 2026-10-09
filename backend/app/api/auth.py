from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth_schema import SignupRequest, LoginRequest
from app.services import auth_service

router = APIRouter()


@router.post("/signup")
def signup(payload: SignupRequest, db: Session = Depends(get_db)):
    visitor = auth_service.signup_visitor(
        db, payload.name, payload.email, payload.phone, payload.password
    )
    return {"success": True, "data": {"visitor_id": visitor.visitor_id}, "message": "Signup successful"}


@router.post("/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    result = auth_service.login_visitor(db, payload.email, payload.password)
    return {"success": True, "data": result, "message": "Login successful"}
