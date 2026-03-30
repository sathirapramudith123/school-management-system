from fastapi import FastAPI, HTTPException, status
from typing import List
from models import Student, StudentCreate, StudentUpdate
from service import StudentService

app = FastAPI(
    title="Student Microservice",
    version="1.0.0"
)

student_service = StudentService()


@app.get("/")
def root():
    return {"message": "Student Microservice is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/students", response_model=List[Student])
def get_all_students():
    return student_service.get_all_students()


@app.get("/students/email/{email}", response_model=Student)
def get_student_by_email(email: str):
    student = student_service.get_student_by_email(email)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.get("/students/grade/{grade}", response_model=List[Student])
def get_students_by_grade(grade: int):
    if grade < 1 or grade > 13:
        raise HTTPException(status_code=400, detail="Grade must be between 1 and 13")
    return student_service.get_students_by_grade(grade)


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = student_service.get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    if student.grade < 1 or student.grade > 13:
        raise HTTPException(status_code=400, detail="Grade must be between 1 and 13")

    new_student = student_service.create_student(student)
    if not new_student:
        raise HTTPException(status_code=400, detail="Email already exists")

    return new_student


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentUpdate):
    if student.grade is not None and (student.grade < 1 or student.grade > 13):
        raise HTTPException(status_code=400, detail="Grade must be between 1 and 13")

    updated_student = student_service.update_student(student_id, student)

    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    if updated_student == "email_exists":
        raise HTTPException(status_code=400, detail="Email already exists")

    return updated_student


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    success = student_service.delete_student(student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)