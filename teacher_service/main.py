from fastapi import FastAPI, HTTPException, status
from typing import List
from models import Teacher, TeacherCreate, TeacherUpdate
from service import TeacherService

app = FastAPI(
    title="Teacher Microservice",
    version="1.0.0"
)

teacher_service = TeacherService()


@app.get("/")
def root():
    return {"message": "Teacher Microservice is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/teachers", response_model=List[Teacher])
def get_all_teachers():
    return teacher_service.get_all_teachers()


@app.get("/teachers/email/{email}", response_model=Teacher)
def get_teacher_by_email(email: str):
    teacher = teacher_service.get_teacher_by_email(email)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher


@app.get("/teachers/specialization/{specialization}", response_model=List[Teacher])
def get_teachers_by_specialization(specialization: str):
    return teacher_service.get_teachers_by_specialization(specialization)


@app.get("/teachers/{teacher_id}", response_model=Teacher)
def get_teacher(teacher_id: int):
    teacher = teacher_service.get_teacher_by_id(teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher


@app.post("/teachers", response_model=Teacher, status_code=status.HTTP_201_CREATED)
def create_teacher(teacher: TeacherCreate):
    if teacher.salary is not None and teacher.salary < 0:
        raise HTTPException(status_code=400, detail="Salary cannot be negative")

    new_teacher = teacher_service.create_teacher(teacher)
    if not new_teacher:
        raise HTTPException(status_code=400, detail="Email already exists")

    return new_teacher


@app.put("/teachers/{teacher_id}", response_model=Teacher)
def update_teacher(teacher_id: int, teacher: TeacherUpdate):
    if teacher.salary is not None and teacher.salary < 0:
        raise HTTPException(status_code=400, detail="Salary cannot be negative")

    updated_teacher = teacher_service.update_teacher(teacher_id, teacher)

    if updated_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")

    if updated_teacher == "email_exists":
        raise HTTPException(status_code=400, detail="Email already exists")

    return updated_teacher


@app.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: int):
    success = teacher_service.delete_teacher(teacher_id)
    if not success:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return {"message": "Teacher deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)