# 📊 Attendance Microservice (FastAPI)

A simple **Attendance Management Microservice** built using **FastAPI** with in-memory mock data.
This service provides REST APIs to track and manage student attendance records.

---

## 🚀 Features

* 📋 Get all attendance records
* 🔍 Get attendance by ID
* 👨‍🎓 Get attendance by student
* 📚 Get attendance by course
* ➕ Create attendance record
* ✏️ Update attendance (status & remarks)
* 🗑️ Delete attendance
* ⚡ FastAPI Swagger documentation

---

## 🛠️ Tech Stack

* **Backend**: FastAPI
* **Language**: Python
* **Validation**: Pydantic
* **Server**: Uvicorn

---

## 📦 Installation & Setup

### 1. Clone the repository

```bash id="n8hv8g"
git clone https://github.com/your-username/attendance-microservice.git
cd attendance-microservice
```

### 2. Create virtual environment

```bash id="xib4b5"
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash id="ckd87s"
pip install fastapi uvicorn httpx
```

### 4. Run the server

```bash id="wq1gfw"
uvicorn main:app --reload --port 8005
```

---

## 🌐 Base URL

```bash id="dmqqpm"
http://localhost:8005
```

---

## 📖 API Endpoints

### 🔹 Health Check

```http id="e63r8z"
GET /health
```

---

### 🔹 Get All Attendance

```http id="4qtz4s"
GET /attendance
```

---

### 🔹 Get Attendance by ID

```http id="ub3vpy"
GET /attendance/{attendance_id}
```

---

### 🔹 Get Attendance by Student

```http id="ju07qu"
GET /attendance/student/{student_id}
```

---

### 🔹 Get Attendance by Course

```http id="36r4hy"
GET /attendance/course/{course_id}
```

---

### 🔹 Create Attendance

```http id="ufqsxx"
POST /attendance
```

#### Request Body

```json id="qf75jk"
{
  "student_id": 1,
  "course_id": 101,
  "status": "present",
  "marked_by": 1,
  "remarks": "On time"
}
```

---

### 🔹 Update Attendance

```http id="l74b3o"
PUT /attendance/{attendance_id}
```

#### Request Body

```json id="wzkhfd"
{
  "status": "late",
  "remarks": "Arrived late"
}
```

---

### 🔹 Delete Attendance

```http id="ykzwnk"
DELETE /attendance/{attendance_id}
```

---

## 🧪 Testing with Postman

1. Open Postman
2. Select HTTP method (GET, POST, PUT, DELETE)
3. Use base URL:

```bash id="2qb80w"
http://localhost:8005
```

4. Add header:

```makefile id="i1mq0r"
Content-Type: application/json
```

5. Send request

---

## 📄 Example Response

```json id="bqzk0c"
{
  "id": 1,
  "student_id": 1,
  "course_id": 101,
  "date": "2026-04-22",
  "status": "present",
  "marked_by": 1,
  "remarks": "On time",
  "marked_at": "2026-04-22T10:00:00"
}
```

---

## ⚠️ Validation Rules

* Status must be one of:
  **present, absent, late, excused**
* Only one attendance record per:
  **student + course + date**
* Attendance record must exist for update/delete

---

## 📚 API Documentation

FastAPI provides built-in interactive docs:

* Swagger UI:

```bash id="u4a6qn"
http://localhost:8005/docs
```

* ReDoc:

```bash id="ph0qec"
http://localhost:8005/redoc
```

---

## 🔮 Future Improvements

* 🔗 Integrate with Student & Course microservices
* 🔐 Add authentication (JWT)
* 📊 Attendance analytics & reports
* 🧪 Add automated testing

---

## 👨‍💻 Author

Developed as part of a **microservices-based system**.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
