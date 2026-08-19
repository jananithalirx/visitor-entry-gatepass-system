from sqlalchemy.orm import Session

from app.models.models import GatePass


def create_gate_pass(db: Session, visitor_id: str, host_id: str, purpose: str, valid_from, valid_to):
    gate_pass = GatePass(
        visitor_id=visitor_id,
        host_id=host_id,
        purpose=purpose,
        valid_from=valid_from,
        valid_to=valid_to,
        status="PENDING",
    )
    db.add(gate_pass)
    db.commit()
    db.refresh(gate_pass)
    return gate_pass


def list_gate_passes_for_visitor(db: Session, visitor_id: str):
    return db.query(GatePass).filter(GatePass.visitor_id == visitor_id).all()


def approve_gate_pass(db: Session, pass_id: str):
    gate_pass = db.query(GatePass).filter(GatePass.pass_id == pass_id).first()
    if gate_pass:
        gate_pass.status = "APPROVED"
        db.commit()
        db.refresh(gate_pass)
    return gate_pass
