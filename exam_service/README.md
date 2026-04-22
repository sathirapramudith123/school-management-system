# 📝 Exam Microservice (FastAPI)

A simple **Exam & Results Management Microservice** built using **FastAPI** with in-memory mock data.
This service provides REST APIs to manage exams and student results, including grade calculation.

---

## 🚀 Features

### 🎓 Exam Management

* 📋 Get all exams
* 🔍 Get exam by ID
* 📚 Get exams by course
* ➕ Create exam
* ✏️ Update exam
* 🗑️ Delete exam

### 📊 Result Management

* 📋 Get all results
* 🔍 Get result by ID
* 👨‍🎓 Get results by student
* 📚 Get results by exam
* ➕ Create result (auto grade calculation)
* ✏️ Update result (recalculate grade)
* 🗑️ Delete result

---

## 🛠️ Tech Stack

* **Backend**: FastAPI
* **Language**: Python
* **Validation**: Pydantic
* **Server**: Uvicorn

---

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/exam-microservice.git
cd exam-microservice
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn httpx
```

### 4. Run the server

```bash
uvicorn main:app --reload --port 8006
```

---

## 🌐 Base URL

```bash
http://localhost:8006
```

---

## 📖 API Endpoints

### 🔹 Health Check

```http
GET /health
```

---

## 🎓 Exam Endpoints

### 🔹 Get All Exams

```http
GET /exams
```

### 🔹 Get Exam by ID

```http
GET /exams/{exam_id}
```

### 🔹 Get Exams by Course

```http
GET /exams/course/{course_id}
```

### 🔹 Create Exam

```http
POST /exams
```

#### Request Body

```json
{
  "name": "Chemistry Quiz",
  "course_id": 103,
  "exam_date": "2026-06-10",
  "duration_minutes": 60,
  "total_marks": 50,
  "passing_marks": 20,
  "exam_type": "quiz"
}
```

---

### 🔹 Update Exam

```http
PUT /exams/{exam_id}
```

---

### 🔹 Delete Exam

```http
DELETE /exams/{exam_id}
```

---

## 📊 Result Endpoints

### 🔹 Get All Results

```http
GET /results
```

### 🔹 Get Result by ID

```http
GET /results/{result_id}
```

### 🔹 Get Results by Exam

```http
GET /results/exam/{exam_id}
```

### 🔹 Get Results by Student

```http
GET /results/student/{student_id}
```

### 🔹 Create Result

```http
POST /results
```

#### Request Body

```json
{
  "exam_id": 1,
  "student_id": 3,
  "marks_obtained": 68,
  "remarks": "Well done"
}
```

---

### 🔹 Update Result

```http
PUT /results/{result_id}
```

---

### 🔹 Delete Result

```http
DELETE /results/{result_id}
```

---

## 🧪 Testing with Postman

1. Open Postman
2. Select HTTP method (GET, POST, PUT, DELETE)
3. Use base URL:

```bash
http://localhost:8006
```

4. Add header:

```makefile
Content-Type: application/json
```

5. Send request

---

## 📄 Example Response

```json
{
  "id": 1,
  "exam_id": 1,
  "student_id": 1,
  "marks_obtained": 78,
  "grade": "A",
  "remarks": "Good job"
}
```

---

## ⚠️ Validation Rules

* Total marks must be **greater than 0**
* Passing marks cannot exceed total marks
* Marks must be within valid range (0 - total marks)
* Exam must exist before creating results
* Grades are automatically calculated based on percentage

---

## 🧠 Grade Calculation Logic

| Percentage | Grade |
| ---------- | ----- |
| ≥ 75%      | A     |
| ≥ 65%      | B     |
| ≥ 55%      | C     |
| ≥ 40%      | S     |
| < 40%      | F     |

---

## 📚 API Documentation

FastAPI provides built-in interactive docs:

* Swagger UI:

```bash
http://localhost:8006/docs
```

* ReDoc:

```bash
http://localhost:8006/redoc
```

---

## 🔮 Future Improvements

* 🔗 Integrate with Student & Course microservices
* 🔐 Add authentication (JWT)
* 📊 Exam analytics & performance dashboards
* 🧪 Add automated testing

---

## 👨‍💻 Author

Developed as part of a **microservices-based system **.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
