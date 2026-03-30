from pydantic import BaseModel
from typing import Optional


class Attendance(BaseModel):
    id: int
    student_id: int
    course_id: int
    date: str
    status: str
    marked_by: Optional[int] = None
    remarks: Optional[str] = None
    marked_at: str


class AttendanceCreate(BaseModel):
    student_id: int
    course_id: int
    date: Optional[str] = None
    status: str
    marked_by: Optional[int] = None
    remarks: Optional[str] = None


class AttendanceUpdate(BaseModel):
    status: Optional[str] = None
    remarks: Optional[str] = None