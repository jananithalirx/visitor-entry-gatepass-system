from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth_schema import LoginRequest, SignupRequest
from app.services import auth_service

router = APIRouter()


@router.post("/signup")
def signup(data: SignupRequest, db: Session = Depends(get_db)):
    visitor = auth_service.signup_visitor(
        db,
        data.name,
        data.email,
        data.phone,
        data.password
    )

    return {
        "success": True,
        "data": {"visitor_id": visitor.visitor_id},
        "message": "Signup successful"
    }


@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    result = auth_service.login_visitor(
        db,
        data.email,
        data.password
    )

    return {
        "success": True,
        "data": result,
        "message": "Login successful"
    }
