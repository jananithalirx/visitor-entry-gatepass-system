from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class VisitorOut(BaseModel):
    visitor_id: str
    name: str
    phone: str
    email: Optional[str] = None

    class Config:
        from_attributes = True


class GatePassCreate(BaseModel):
    visitor_id: str
    host_id: str
    purpose: str
    valid_from: datetime
    valid_to: datetime


class GatePassOut(BaseModel):
    pass_id: str
    visitor_id: str
    host_id: str
    purpose: Optional[str]
    status: str
    valid_from: datetime
    valid_to: datetime

    class Config:
        from_attributes = True
