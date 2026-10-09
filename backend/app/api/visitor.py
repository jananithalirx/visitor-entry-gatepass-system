from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.models import Visitor
from app.schemas.visitor_schema import VisitorOut

router = APIRouter()


@router.get("/{visitor_id}", response_model=VisitorOut)
def get_visitor(visitor_id: str, db: Session = Depends(get_db)):
    return db.query(Visitor).filter(Visitor.visitor_id == visitor_id).first()


@router.get("/")
def list_visitors(db: Session = Depends(get_db)):
    visitors = db.query(Visitor).all()
    return {"success": True, "data": visitors, "message": "Visitors fetched"}
