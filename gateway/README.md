# 🌐 School Management API Gateway (FastAPI)

A centralized **API Gateway** built using **FastAPI** to manage and route requests across multiple microservices in the School Management System.

This gateway acts as a **single entry point** for all client requests and forwards them to the appropriate microservices.

---

## 🚀 Features

* 🌐 Centralized API Gateway
* 🔗 Routes requests to multiple microservices
* ⚡ Asynchronous request forwarding using `httpx`
* 🛡️ Error handling (timeout, service offline, etc.)
* 📦 Supports all CRUD operations across services
* 📊 Health monitoring

---

## 🧩 Connected Microservices

| Service            | Port | Base URL              |
| ------------------ | ---- | --------------------- |
| Student Service    | 8001 | `/gateway/students`   |
| Teacher Service    | 8002 | `/gateway/teachers`   |
| Course Service     | 8003 | `/gateway/courses`    |
| Classroom Service  | 8004 | `/gateway/classrooms` |
| Attendance Service | 8005 | `/gateway/attendance` |
| Exam Service       | 8006 | `/gateway/exams`      |
| Exam Results       | 8006 | `/gateway/results`    |

---

## 🛠️ Tech Stack

* **Framework**: FastAPI
* **Language**: Python
* **HTTP Client**: httpx
* **Server**: Uvicorn

---

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/api-gateway.git
cd api-gateway
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
uvicorn main:app --reload --port 8000
```

---

## 🌐 Base URL

```bash
http://localhost:8000
```

---

## 📖 API Gateway Endpoints

### 🔹 Health Check

```http
GET /health
```

---

## 🔗 Student Routes

```http
GET    /gateway/students
GET    /gateway/students/{id}
POST   /gateway/students
PUT    /gateway/students/{id}
DELETE /gateway/students/{id}
```

---

## 👩‍🏫 Teacher Routes

```http
GET    /gateway/teachers
GET    /gateway/teachers/{id}
POST   /gateway/teachers
PUT    /gateway/teachers/{id}
DELETE /gateway/teachers/{id}
```

---

## 📚 Course Routes

```http
GET    /gateway/courses
GET    /gateway/courses/{id}
POST   /gateway/courses
PUT    /gateway/courses/{id}
DELETE /gateway/courses/{id}
```

---

## 🏫 Classroom Routes

```http
GET    /gateway/classrooms
GET    /gateway/classrooms/{id}
POST   /gateway/classrooms
PUT    /gateway/classrooms/{id}
DELETE /gateway/classrooms/{id}
```

---

## 📊 Attendance Routes

```http
GET    /gateway/attendance
GET    /gateway/attendance/{id}
POST   /gateway/attendance
PUT    /gateway/attendance/{id}
DELETE /gateway/attendance/{id}
```

---

## 📝 Exam Routes

```http
GET    /gateway/exams
GET    /gateway/exams/{id}
POST   /gateway/exams
PUT    /gateway/exams/{id}
DELETE /gateway/exams/{id}
```

---

## 📈 Result Routes

```http
GET    /gateway/results
GET    /gateway/results/{id}
POST   /gateway/results
PUT    /gateway/results/{id}
DELETE /gateway/results/{id}
```

---

## 🧪 Testing with Postman

1. Open Postman
2. Use base URL:

```bash
http://localhost:8000
```

3. Example:

```bash
GET http://localhost:8000/gateway/students
```

4. For POST/PUT:

```makefile
Content-Type: application/json
```

---

## ⚠️ Error Handling

The API Gateway handles common errors:

| Error | Description           |
| ----- | --------------------- |
| 404   | Service not found     |
| 503   | Microservice offline  |
| 504   | Request timeout       |
| 500   | Internal server error |

---

## 🔄 Request Flow

```
Client → API Gateway → Microservice → Response → Gateway → Client
```

---

## 📚 API Documentation

FastAPI provides built-in docs:

* Swagger UI:

```bash
http://localhost:8000/docs
```

* ReDoc:

```bash
http://localhost:8000/redoc
```

---

## 🔮 Future Improvements

* 🔐 Authentication (JWT / API Keys)
* ⚖️ Load balancing
* 📊 Request logging & monitoring
* 🚦 Rate limiting
* 🔗 Service discovery

---

## 👨‍💻 Author

Developed as part of a **microservices-based School Management System**.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
