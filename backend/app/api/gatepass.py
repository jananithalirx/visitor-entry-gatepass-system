from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.visitor_schema import GatePassCreate
from app.services import gatepass_service

router = APIRouter()


@router.post("/")
def create_pass(payload: GatePassCreate, db: Session = Depends(get_db)):
    gate_pass = gatepass_service.create_gate_pass(
        db, payload.visitor_id, payload.host_id, payload.purpose,
        payload.valid_from, payload.valid_to,
    )
    return {"success": True, "data": {"pass_id": gate_pass.pass_id, "status": gate_pass.status}, "message": "Gate pass created"}


@router.get("/visitor/{visitor_id}")
def list_passes(visitor_id: str, db: Session = Depends(get_db)):
    passes = gatepass_service.list_gate_passes_for_visitor(db, visitor_id)
    return {"success": True, "data": passes, "message": "Gate passes fetched"}


@router.patch("/{pass_id}/approve")
def approve_pass(pass_id: str, db: Session = Depends(get_db)):
    gate_pass = gatepass_service.approve_gate_pass(db, pass_id)
    return {"success": True, "data": {"pass_id": pass_id, "status": gate_pass.status}, "message": "Gate pass approved"}
