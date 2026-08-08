from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.models import Visitor
from app.core.security import hash_password, verify_password, create_access_token


def signup_visitor(db: Session, name: str, email: str, phone: str, password: str):
    existing = db.query(Visitor).filter(Visitor.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    visitor = Visitor(
        name=name,
        email=email,
        phone=phone,
        hashed_password=hash_password(password),
    )
    db.add(visitor)
    db.commit()
    db.refresh(visitor)
    return visitor


def login_visitor(db: Session, email: str, password: str):
    visitor = db.query(Visitor).filter(Visitor.email == email).first()
    if not visitor or not verify_password(password, visitor.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": visitor.visitor_id, "role": "visitor"})
    return {"access_token": token, "token_type": "bearer", "visitor_id": visitor.visitor_id}
