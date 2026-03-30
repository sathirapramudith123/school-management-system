from fastapi import FastAPI, HTTPException, status
from typing import List
from models import Course, CourseCreate, CourseUpdate
from service import CourseService

app = FastAPI(
    title="Course Microservice",
    version="1.0.0"
)

course_service = CourseService()


@app.get("/")
def root():
    return {"message": "Course Microservice is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/courses", response_model=List[Course])
def get_all_courses():
    return course_service.get_all_courses()


@app.get("/courses/code/{code}", response_model=Course)
def get_course_by_code(code: str):
    course = course_service.get_course_by_code(code)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@app.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: int):
    course = course_service.get_course_by_id(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@app.post("/courses", response_model=Course, status_code=status.HTTP_201_CREATED)
def create_course(course: CourseCreate):
    if course.credits <= 0:
        raise HTTPException(status_code=400, detail="Credits must be greater than 0")

    new_course = course_service.create_course(course)
    if not new_course:
        raise HTTPException(status_code=400, detail="Course code already exists")

    return new_course


@app.put("/courses/{course_id}", response_model=Course)
def update_course(course_id: int, course: CourseUpdate):
    if course.credits is not None and course.credits <= 0:
        raise HTTPException(status_code=400, detail="Credits must be greater than 0")

    updated_course = course_service.update_course(course_id, course)

    if updated_course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    if updated_course == "code_exists":
        raise HTTPException(status_code=400, detail="Course code already exists")

    return updated_course


@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    success = course_service.delete_course(course_id)
    if not success:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8003, reload=True)