from pydantic import BaseModel
from typing import Optional


class Exam(BaseModel):
    id: int
    name: str
    course_id: int
    exam_date: str
    duration_minutes: int
    total_marks: int
    passing_marks: int
    exam_type: str


class ExamCreate(BaseModel):
    name: str
    course_id: int
    exam_date: str
    duration_minutes: int
    total_marks: int
    passing_marks: int
    exam_type: str


class ExamUpdate(BaseModel):
    name: Optional[str] = None
    exam_date: Optional[str] = None
    duration_minutes: Optional[int] = None
    total_marks: Optional[int] = None
    passing_marks: Optional[int] = None
    exam_type: Optional[str] = None


class ExamResult(BaseModel):
    id: int
    exam_id: int
    student_id: int
    marks_obtained: float
    grade: str
    remarks: Optional[str] = None


class ExamResultCreate(BaseModel):
    exam_id: int
    student_id: int
    marks_obtained: float
    remarks: Optional[str] = None


class ExamResultUpdate(BaseModel):
    marks_obtained: Optional[float] = None
    remarks: Optional[str] = None