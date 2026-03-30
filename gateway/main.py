from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import httpx

app = FastAPI(
    title="School Management API Gateway",
    version="1.0.0"
)

# Microservice URLs
SERVICES = {
    "student": "http://127.0.0.1:8001",
    "teacher": "http://127.0.0.1:8002",
    "course": "http://127.0.0.1:8003",
    "classroom": "http://127.0.0.1:8004",
    "attendance": "http://127.0.0.1:8005",
    "exam": "http://127.0.0.1:8006"
}


@app.get("/")
def root():
    return {
        "message": "School Management API Gateway is running",
        "services": list(SERVICES.keys())
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "gateway_port": 8000
    }


async def forward_request(service_name: str, path: str, method: str, body=None):
    if service_name not in SERVICES:
        raise HTTPException(status_code=404, detail="Service not found")

    url = f"{SERVICES[service_name]}{path}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method=method,
                url=url,
                json=body,
                timeout=10.0
            )

        try:
            content = response.json()
        except:
            content = {"message": response.text}

        return JSONResponse(status_code=response.status_code, content=content)

    except httpx.ConnectError:
        raise HTTPException(status_code=503, detail=f"{service_name} service is offline")

    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail=f"{service_name} service timeout")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =========================
# Student Routes
# =========================

@app.get("/gateway/students")
async def get_students():
    return await forward_request("student", "/students", "GET")


@app.get("/gateway/students/{student_id}")
async def get_student(student_id: int):
    return await forward_request("student", f"/students/{student_id}", "GET")


@app.post("/gateway/students")
async def create_student(request: Request):
    body = await request.json()
    return await forward_request("student", "/students", "POST", body)


@app.put("/gateway/students/{student_id}")
async def update_student(student_id: int, request: Request):
    body = await request.json()
    return await forward_request("student", f"/students/{student_id}", "PUT", body)


@app.delete("/gateway/students/{student_id}")
async def delete_student(student_id: int):
    return await forward_request("student", f"/students/{student_id}", "DELETE")


# =========================
# Teacher Routes
# =========================

@app.get("/gateway/teachers")
async def get_teachers():
    return await forward_request("teacher", "/teachers", "GET")


@app.get("/gateway/teachers/{teacher_id}")
async def get_teacher(teacher_id: int):
    return await forward_request("teacher", f"/teachers/{teacher_id}", "GET")


@app.post("/gateway/teachers")
async def create_teacher(request: Request):
    body = await request.json()
    return await forward_request("teacher", "/teachers", "POST", body)


@app.put("/gateway/teachers/{teacher_id}")
async def update_teacher(teacher_id: int, request: Request):
    body = await request.json()
    return await forward_request("teacher", f"/teachers/{teacher_id}", "PUT", body)


@app.delete("/gateway/teachers/{teacher_id}")
async def delete_teacher(teacher_id: int):
    return await forward_request("teacher", f"/teachers/{teacher_id}", "DELETE")


# =========================
# Course Routes
# =========================

@app.get("/gateway/courses")
async def get_courses():
    return await forward_request("course", "/courses", "GET")


@app.get("/gateway/courses/{course_id}")
async def get_course(course_id: int):
    return await forward_request("course", f"/courses/{course_id}", "GET")


@app.post("/gateway/courses")
async def create_course(request: Request):
    body = await request.json()
    return await forward_request("course", "/courses", "POST", body)


@app.put("/gateway/courses/{course_id}")
async def update_course(course_id: int, request: Request):
    body = await request.json()
    return await forward_request("course", f"/courses/{course_id}", "PUT", body)


@app.delete("/gateway/courses/{course_id}")
async def delete_course(course_id: int):
    return await forward_request("course", f"/courses/{course_id}", "DELETE")


# =========================
# Classroom Routes
# =========================

@app.get("/gateway/classrooms")
async def get_classrooms():
    return await forward_request("classroom", "/classrooms", "GET")


@app.get("/gateway/classrooms/{classroom_id}")
async def get_classroom(classroom_id: int):
    return await forward_request("classroom", f"/classrooms/{classroom_id}", "GET")


@app.post("/gateway/classrooms")
async def create_classroom(request: Request):
    body = await request.json()
    return await forward_request("classroom", "/classrooms", "POST", body)


@app.put("/gateway/classrooms/{classroom_id}")
async def update_classroom(classroom_id: int, request: Request):
    body = await request.json()
    return await forward_request("classroom", f"/classrooms/{classroom_id}", "PUT", body)


@app.delete("/gateway/classrooms/{classroom_id}")
async def delete_classroom(classroom_id: int):
    return await forward_request("classroom", f"/classrooms/{classroom_id}", "DELETE")


# =========================
# Attendance Routes
# =========================

@app.get("/gateway/attendance")
async def get_attendance():
    return await forward_request("attendance", "/attendance", "GET")


@app.get("/gateway/attendance/{attendance_id}")
async def get_attendance_by_id(attendance_id: int):
    return await forward_request("attendance", f"/attendance/{attendance_id}", "GET")


@app.post("/gateway/attendance")
async def create_attendance(request: Request):
    body = await request.json()
    return await forward_request("attendance", "/attendance", "POST", body)


@app.put("/gateway/attendance/{attendance_id}")
async def update_attendance(attendance_id: int, request: Request):
    body = await request.json()
    return await forward_request("attendance", f"/attendance/{attendance_id}", "PUT", body)


@app.delete("/gateway/attendance/{attendance_id}")
async def delete_attendance(attendance_id: int):
    return await forward_request("attendance", f"/attendance/{attendance_id}", "DELETE")


# =========================
# Exam Routes
# =========================

@app.get("/gateway/exams")
async def get_exams():
    return await forward_request("exam", "/exams", "GET")


@app.get("/gateway/exams/{exam_id}")
async def get_exam(exam_id: int):
    return await forward_request("exam", f"/exams/{exam_id}", "GET")


@app.post("/gateway/exams")
async def create_exam(request: Request):
    body = await request.json()
    return await forward_request("exam", "/exams", "POST", body)


@app.put("/gateway/exams/{exam_id}")
async def update_exam(exam_id: int, request: Request):
    body = await request.json()
    return await forward_request("exam", f"/exams/{exam_id}", "PUT", body)


@app.delete("/gateway/exams/{exam_id}")
async def delete_exam(exam_id: int):
    return await forward_request("exam", f"/exams/{exam_id}", "DELETE")


# =========================
# Exam Result Routes
# =========================

@app.get("/gateway/results")
async def get_results():
    return await forward_request("exam", "/results", "GET")


@app.get("/gateway/results/{result_id}")
async def get_result(result_id: int):
    return await forward_request("exam", f"/results/{result_id}", "GET")


@app.post("/gateway/results")
async def create_result(request: Request):
    body = await request.json()
    return await forward_request("exam", "/results", "POST", body)


@app.put("/gateway/results/{result_id}")
async def update_result(result_id: int, request: Request):
    body = await request.json()
    return await forward_request("exam", f"/results/{result_id}", "PUT", body)


@app.delete("/gateway/results/{result_id}")
async def delete_result(result_id: int):
    return await forward_request("exam", f"/results/{result_id}", "DELETE")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)