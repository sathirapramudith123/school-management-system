# 📚 Course Microservice (FastAPI)

A lightweight **Course Management Microservice** built using **FastAPI** with in-memory mock data.
This service provides REST APIs to manage courses including create, read, update, and delete operations.

---

## 🚀 Features

* 📖 Get all courses
* 🔍 Get course by ID / Code
* ➕ Create new course
* ✏️ Update course details
* 🗑️ Delete course
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

```bash
git clone https://github.com/your-username/course-microservice.git
cd course-microservice
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
uvicorn main:app --reload --port 8003
```

---

## 🌐 Base URL

```bash
http://localhost:8003
```

---

## 📖 API Endpoints

### 🔹 Health Check

```http
GET /health
```

---

### 🔹 Get All Courses

```http
GET /courses
```

---

### 🔹 Get Course by ID

```http
GET /courses/{course_id}
```

---

### 🔹 Get Course by Code

```http
GET /courses/code/{code}
```

---

### 🔹 Create Course

```http
POST /courses
```

#### Request Body

```json
{
  "name": "Software Engineering",
  "code": "SE401",
  "credits": 4
}
```

---

### 🔹 Update Course

```http
PUT /courses/{course_id}
```

#### Request Body (Partial Update Allowed)

```json
{
  "name": "Advanced Software Engineering",
  "credits": 5
}
```

---

### 🔹 Delete Course

```http
DELETE /courses/{course_id}
```

---

## 🧪 Testing with Postman

1. Open Postman
2. Set method (GET, POST, PUT, DELETE)
3. Use base URL:

```bash
http://localhost:8003
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
  "name": "Computer Science",
  "code": "CS101",
  "credits": 3
}
```

---

## ⚠️ Validation Rules

* Credits must be **greater than 0**
* Course code must be **unique**
* Course must exist for update/delete operations

---

## 📚 API Documentation

FastAPI provides built-in interactive docs:

* Swagger UI:

```bash
http://localhost:8003/docs
```

* ReDoc:

```bash
http://localhost:8003/redoc
```

---

## 🔮 Future Improvements

* 🔗 Integrate with database (MongoDB / PostgreSQL)
* 🔐 Add authentication (JWT)
* 📊 Add pagination & filtering
* 🧪 Add automated tests

---

## 👨‍💻 Author

Developed as part of a **microservices-based system**.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
