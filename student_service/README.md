# 🎓 Student Microservice (FastAPI)

A simple **Student Management Microservice** built using **FastAPI** with in-memory mock data.
This service provides REST APIs to manage students including create, read, update, and delete operations.

---

## 🚀 Features

* ✅ Get all students
* 🔍 Get student by ID / Email
* 🎓 Filter students by grade
* ➕ Create new student
* ✏️ Update student details
* 🗑️ Delete student
* ⚡ FastAPI automatic Swagger docs

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
git clone https://github.com/your-username/student-microservice.git
cd student-microservice
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn
```

### 4. Run the server

```bash
uvicorn main:app --reload --port 8001
```

---

## 🌐 Base URL

```
http://localhost:8001
```

---

## 📖 API Endpoints

### 🔹 Health Check

```
GET /health
```

---

### 🔹 Get All Students

```
GET /students
```

---

### 🔹 Get Student by ID

```
GET /students/{student_id}
```

---

### 🔹 Get Student by Email

```
GET /students/email/{email}
```

---

### 🔹 Get Students by Grade

```
GET /students/grade/{grade}
```

---

### 🔹 Create Student

```
POST /students
```

#### Request Body

```json
{
  "first_name": "Saman",
  "last_name": "Fernando",
  "email": "saman.fernando@school.com",
  "phone": "0712345678",
  "date_of_birth": "2012-03-10",
  "grade": 8,
  "address": "Galle"
}
```

---

### 🔹 Update Student

```
PUT /students/{student_id}
```

#### Request Body (Partial Update Allowed)

```json
{
  "first_name": "Updated Name",
  "grade": 11
}
```

---

### 🔹 Delete Student

```
DELETE /students/{student_id}
```

---

## 🧪 Testing with Postman

1. Open Postman
2. Set method (GET, POST, PUT, DELETE)
3. Use base URL:

```
http://localhost:8001
```

4. Add header:

```
Content-Type: application/json
```

5. Send request

---

## 📄 Example Response

```json
{
  "id": 1,
  "first_name": "Kamal",
  "last_name": "Perera",
  "email": "kamal.perera@school.com",
  "phone": "0771234567",
  "date_of_birth": "2010-05-15",
  "grade": 10,
  "address": "Colombo",
  "enrolled_date": "2024-01-15"
}
```

---

## ⚠️ Validation Rules

* Grade must be between **1 and 13**
* Email must be **unique**
* Student must exist for update/delete operations

---

## 📚 API Documentation

FastAPI provides built-in interactive docs:

* Swagger UI:

```
http://localhost:8001/docs
```

* ReDoc:

```
http://localhost:8001/redoc
```

---

## 🔮 Future Improvements

* 🔗 Connect to MongoDB Atlas
* 🔐 Add authentication (JWT)
* 📊 Add pagination & filtering
* 🧪 Add automated tests

---

## 👨‍💻 Author

Developed as part of a **microservices-based system / research project**.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
