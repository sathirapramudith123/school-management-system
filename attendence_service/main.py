from fastapi import FastAPI, HTTPException, status
from typing import List
from models import Attendance, AttendanceCreate, AttendanceUpdate
from service import AttendanceService

app = FastAPI(
    title="Attendance Microservice",
    version="1.0.0"
)

attendance_service = AttendanceService()
VALID_STATUSES = ["present", "absent", "late", "excused"]


@app.get("/")
def root():
    return {"message": "Attendance Microservice is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/attendance", response_model=List[Attendance])
def get_all_attendance():
    return attendance_service.get_all_attendance()


@app.get("/attendance/student/{student_id}", response_model=List[Attendance])
def get_attendance_by_student(student_id: int):
    return attendance_service.get_attendance_by_student(student_id)


@app.get("/attendance/course/{course_id}", response_model=List[Attendance])
def get_attendance_by_course(course_id: int):
    return attendance_service.get_attendance_by_course(course_id)


@app.get("/attendance/{attendance_id}", response_model=Attendance)
def get_attendance(attendance_id: int):
    record = attendance_service.get_attendance_by_id(attendance_id)
    if not record:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return record


@app.post("/attendance", response_model=Attendance, status_code=status.HTTP_201_CREATED)
def create_attendance(attendance: AttendanceCreate):
    if attendance.status.lower() not in VALID_STATUSES:
        raise HTTPException(
            status_code=400,
            detail=f"Status must be one of {VALID_STATUSES}"
        )

    new_record = attendance_service.create_attendance(attendance)
    if not new_record:
        raise HTTPException(
            status_code=400,
            detail="Attendance already exists for this student, course, and date"
        )

    return new_record


@app.put("/attendance/{attendance_id}", response_model=Attendance)
def update_attendance(attendance_id: int, attendance: AttendanceUpdate):
    if attendance.status is not None and attendance.status.lower() not in VALID_STATUSES:
        raise HTTPException(
            status_code=400,
            detail=f"Status must be one of {VALID_STATUSES}"
        )

    updated_record = attendance_service.update_attendance(attendance_id, attendance)
    if not updated_record:
        raise HTTPException(status_code=404, detail="Attendance record not found")

    return updated_record


@app.delete("/attendance/{attendance_id}")
def delete_attendance(attendance_id: int):
    success = attendance_service.delete_attendance(attendance_id)
    if not success:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return {"message": "Attendance deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8005, reload=True)