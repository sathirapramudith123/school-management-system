# 👩‍🏫 Teacher Microservice (FastAPI)

A simple **Teacher Management Microservice** built using **FastAPI** with in-memory mock data.
This service provides REST APIs to manage teacher information including creation, retrieval, updates, and deletion.

---

## 🚀 Features

* 👩‍🏫 Get all teachers
* 🔍 Get teacher by ID / Email
* 📘 Filter teachers by specialization
* ➕ Create new teacher
* ✏️ Update teacher details
* 🗑️ Delete teacher
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

```bash id="txd33h"
git clone https://github.com/your-username/teacher-microservice.git
cd teacher-microservice
```

### 2. Create virtual environment

```bash id="mynaj1"
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash id="td23pz"
pip install fastapi uvicorn httpx
```

### 4. Run the server

```bash id="og9dyh"
uvicorn main:app --reload --port 8002
```

---

## 🌐 Base URL

```bash id="v6z9h5"
http://localhost:8002
```

---

## 📖 API Endpoints

### 🔹 Health Check

```http id="qkn32y"
GET /health
```

---

### 🔹 Get All Teachers

```http id="9p1qpl"
GET /teachers
```

---

### 🔹 Get Teacher by ID

```http id="8zgznh"
GET /teachers/{teacher_id}
```

---

### 🔹 Get Teacher by Email

```http id="7d3o2y"
GET /teachers/email/{email}
```

---

### 🔹 Get Teachers by Specialization

```http id="2f8l4x"
GET /teachers/specialization/{specialization}
```

---

### 🔹 Create Teacher

```http id="r1c5oz"
POST /teachers
```

#### Request Body

```json id="fp67fb"
{
  "first_name": "Nadeesha",
  "last_name": "Perera",
  "email": "nadeesha.perera@school.com",
  "phone": "0779998888",
  "specialization": "Chemistry",
  "qualification": "BSc in Chemistry",
  "address": "Galle",
  "salary": 68000
}
```

---

### 🔹 Update Teacher

```http id="vwn7zx"
PUT /teachers/{teacher_id}
```

#### Request Body (Partial Update Allowed)

```json id="jgqrl5"
{
  "salary": 80000,
  "address": "Colombo Updated"
}
```

---

### 🔹 Delete Teacher

```http id="6dq8qc"
DELETE /teachers/{teacher_id}
```

---

## 🧪 Testing with Postman

1. Open Postman
2. Select HTTP method (GET, POST, PUT, DELETE)
3. Use base URL:

```bash id="h1p7ha"
http://localhost:8002
```

4. Add header:

```makefile id="i5lls9"
Content-Type: application/json
```

5. Send request

---

## 📄 Example Response

```json id="w8q12x"
{
  "id": 1,
  "first_name": "Priyanka",
  "last_name": "Wijesinghe",
  "email": "priyanka.wijesinghe@school.com",
  "phone": "0771112233",
  "specialization": "Mathematics",
  "qualification": "BSc in Mathematics",
  "address": "Colombo",
  "joined_date": "2020-01-15",
  "salary": 75000.0
}
```

---

## ⚠️ Validation Rules

* Email must be **unique**
* Salary cannot be **negative**
* Teacher must exist for update/delete

---

## 📚 API Documentation

FastAPI provides built-in interactive docs:

* Swagger UI:

```bash id="mt6q86"
http://localhost:8002/docs
```

* ReDoc:

```bash id="oz6rtb"
http://localhost:8002/redoc
```

---

## 🔮 Future Improvements

* 🔗 Integrate with other microservices (Course, Classroom, etc.)
* 🔐 Add authentication (JWT)
* 📊 Teacher performance analytics
* 🧪 Add automated testing

---

## 👨‍💻 Author

Developed as part of a **microservices-based system**.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
