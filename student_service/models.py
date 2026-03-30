from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    date_of_birth: str
    grade: int
    address: Optional[str] = None
    enrolled_date: str


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    date_of_birth: str
    grade: int
    address: Optional[str] = None


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    grade: Optional[int] = None
    address: Optional[str] = None