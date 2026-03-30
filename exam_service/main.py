from fastapi import FastAPI, HTTPException, status
from typing import List
from models import (
    Exam, ExamCreate, ExamUpdate,
    ExamResult, ExamResultCreate, ExamResultUpdate
)
from service import ExamService

app = FastAPI(
    title="Exam Microservice",
    version="1.0.0"
)

exam_service = ExamService()


@app.get("/")
def root():
    return {"message": "Exam Microservice is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


# ---------- Exam Endpoints ----------

@app.get("/exams", response_model=List[Exam])
def get_all_exams():
    return exam_service.get_all_exams()


@app.get("/exams/course/{course_id}", response_model=List[Exam])
def get_exams_by_course(course_id: int):
    return exam_service.get_exams_by_course(course_id)


@app.get("/exams/{exam_id}", response_model=Exam)
def get_exam(exam_id: int):
    exam = exam_service.get_exam_by_id(exam_id)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    return exam


@app.post("/exams", response_model=Exam, status_code=status.HTTP_201_CREATED)
def create_exam(exam: ExamCreate):
    if exam.passing_marks > exam.total_marks:
        raise HTTPException(status_code=400, detail="Passing marks cannot exceed total marks")

    if exam.total_marks <= 0:
        raise HTTPException(status_code=400, detail="Total marks must be greater than zero")

    return exam_service.create_exam(exam)


@app.put("/exams/{exam_id}", response_model=Exam)
def update_exam(exam_id: int, exam: ExamUpdate):
    updated_exam = exam_service.update_exam(exam_id, exam)
    if not updated_exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    return updated_exam


@app.delete("/exams/{exam_id}")
def delete_exam(exam_id: int):
    success = exam_service.delete_exam(exam_id)
    if not success:
        raise HTTPException(status_code=404, detail="Exam not found")
    return {"message": "Exam deleted successfully"}


# ---------- Result Endpoints ----------

@app.get("/results", response_model=List[ExamResult])
def get_all_results():
    return exam_service.get_all_results()


@app.get("/results/exam/{exam_id}", response_model=List[ExamResult])
def get_results_by_exam(exam_id: int):
    return exam_service.get_results_by_exam(exam_id)


@app.get("/results/student/{student_id}", response_model=List[ExamResult])
def get_results_by_student(student_id: int):
    return exam_service.get_results_by_student(student_id)


@app.get("/results/{result_id}", response_model=ExamResult)
def get_result(result_id: int):
    result = exam_service.get_result_by_id(result_id)
    if not result:
        raise HTTPException(status_code=404, detail="Result not found")
    return result


@app.post("/results", response_model=ExamResult, status_code=status.HTTP_201_CREATED)
def create_result(result: ExamResultCreate):
    exam = exam_service.get_exam_by_id(result.exam_id)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")

    if result.marks_obtained < 0 or result.marks_obtained > exam.total_marks:
        raise HTTPException(status_code=400, detail="Invalid marks")

    new_result = exam_service.create_result(result)
    return new_result


@app.put("/results/{result_id}", response_model=ExamResult)
def update_result(result_id: int, result: ExamResultUpdate):
    existing = exam_service.get_result_by_id(result_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Result not found")

    exam = exam_service.get_exam_by_id(existing.exam_id)

    if result.marks_obtained is not None:
        if result.marks_obtained < 0 or result.marks_obtained > exam.total_marks:
            raise HTTPException(status_code=400, detail="Invalid marks")

    updated_result = exam_service.update_result(result_id, result)
    return updated_result


@app.delete("/results/{result_id}")
def delete_result(result_id: int):
    success = exam_service.delete_result(result_id)
    if not success:
        raise HTTPException(status_code=404, detail="Result not found")
    return {"message": "Result deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8006, reload=True)