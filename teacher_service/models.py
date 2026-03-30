from pydantic import BaseModel
from typing import Optional


class Teacher(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    specialization: str
    qualification: str
    address: Optional[str] = None
    joined_date: str
    salary: Optional[float] = None


class TeacherCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    specialization: str
    qualification: str
    address: Optional[str] = None
    salary: Optional[float] = None


class TeacherUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    specialization: Optional[str] = None
    qualification: Optional[str] = None
    address: Optional[str] = None
    salary: Optional[float] = None