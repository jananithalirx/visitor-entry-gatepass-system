import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from app.core.database import Base


def generate_id():
    return str(uuid.uuid4())


class Visitor(Base):
    __tablename__ = "visitors"

    visitor_id = Column(String, primary_key=True, default=generate_id)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String)
    id_proof_type = Column(String)
    id_proof_number = Column(String)
    hashed_password = Column(String, nullable=False)

    gate_passes = relationship("GatePass", back_populates="visitor")


class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(String, primary_key=True, default=generate_id)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String)
    hashed_password = Column(String, nullable=False)

    gate_passes = relationship("GatePass", back_populates="host")


class GatePass(Base):
    __tablename__ = "gate_passes"

    pass_id = Column(String, primary_key=True, default=generate_id)
    visitor_id = Column(String, ForeignKey("visitors.visitor_id"), nullable=False)
    host_id = Column(String, ForeignKey("employees.employee_id"), nullable=False)
    purpose = Column(String)
    status = Column(String, default="PENDING")
    valid_from = Column(DateTime, default=datetime.utcnow)
    valid_to = Column(DateTime)

    visitor = relationship("Visitor", back_populates="gate_passes")
    host = relationship("Employee", back_populates="gate_passes")


class EntryLog(Base):
    __tablename__ = "entry_logs"

    log_id = Column(String, primary_key=True, default=generate_id)
    pass_id = Column(String, ForeignKey("gate_passes.pass_id"), nullable=False)
    gate = Column(String, default="Main Gate")
    entry_time = Column(DateTime)
    exit_time = Column(DateTime)
