# 🏫 Classroom Microservice (FastAPI)

A simple **Classroom Management Microservice** built using **FastAPI** with in-memory mock data.
This service provides REST APIs to manage classrooms, including creation, retrieval, updates, and deletion.

---

## 🚀 Features

* 🏫 Get all classrooms
* 🔍 Get classroom by ID / Room Number
* 🏢 Filter classrooms by building
* ➕ Create new classroom
* ✏️ Update classroom details
* 🗑️ Delete classroom
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
git clone https://github.com/your-username/classroom-microservice.git
cd classroom-microservice
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
uvicorn main:app --reload --port 8004
```

---

## 🌐 Base URL

```bash
http://localhost:8004
```

---

## 📖 API Endpoints

### 🔹 Health Check

```http
GET /health
```

---

### 🔹 Get All Classrooms

```http
GET /classrooms
```

---

### 🔹 Get Classroom by ID

```http
GET /classrooms/{classroom_id}
```

---

### 🔹 Get Classroom by Room Number

```http
GET /classrooms/room/{room_number}
```

---

### 🔹 Get Classrooms by Building

```http
GET /classrooms/building/{building}
```

---

### 🔹 Create Classroom

```http
POST /classrooms
```

#### Request Body

```json
{
  "room_number": "C301",
  "building": "Engineering Block",
  "capacity": 50,
  "grade_level": 12,
  "has_projector": true,
  "has_ac": true,
  "has_computers": true,
  "description": "Advanced lab"
}
```

---

### 🔹 Update Classroom

```http
PUT /classrooms/{classroom_id}
```

#### Request Body (Partial Update Allowed)

```json
{
  "capacity": 45,
  "has_ac": false
}
```

---

### 🔹 Delete Classroom

```http
DELETE /classrooms/{classroom_id}
```

---

## 🧪 Testing with Postman

1. Open Postman
2. Select HTTP method (GET, POST, PUT, DELETE)
3. Use base URL:

```bash
http://localhost:8004
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
  "room_number": "A101",
  "building": "Main Building",
  "capacity": 40,
  "grade_level": 10,
  "has_projector": true,
  "has_ac": true,
  "has_computers": false,
  "description": "Grade 10 classroom",
  "created_at": "2024-01-15"
}
```

---

## ⚠️ Validation Rules

* Capacity must be **greater than 0**
* Grade level must be between **1 and 13**
* Room number must be **unique**
* Classroom must exist for update/delete

---

## 📚 API Documentation

FastAPI provides built-in interactive docs:

* Swagger UI:

```bash
http://localhost:8004/docs
```

* ReDoc:

```bash
http://localhost:8004/redoc
```

---

## 🔮 Future Improvements

* 🔗 Integrate with database (MongoDB / PostgreSQL)
* 🔐 Add authentication (JWT)
* 📊 Add advanced filtering & pagination
* 🧪 Add automated tests

---

## 👨‍💻 Author

Developed as part of a **microservices-based system**.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
