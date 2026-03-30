from pydantic import BaseModel
from typing import Optional


class Classroom(BaseModel):
    id: int
    room_number: str
    building: str
    capacity: int
    grade_level: Optional[int] = None
    has_projector: bool = False
    has_ac: bool = False
    has_computers: bool = False
    description: Optional[str] = None
    created_at: str


class ClassroomCreate(BaseModel):
    room_number: str
    building: str
    capacity: int
    grade_level: Optional[int] = None
    has_projector: bool = False
    has_ac: bool = False
    has_computers: bool = False
    description: Optional[str] = None


class ClassroomUpdate(BaseModel):
    room_number: Optional[str] = None
    building: Optional[str] = None
    capacity: Optional[int] = None
    grade_level: Optional[int] = None
    has_projector: Optional[bool] = None
    has_ac: Optional[bool] = None
    has_computers: Optional[bool] = None
    description: Optional[str] = None