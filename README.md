<div align="center">

# 🎯 School Management System


[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-222222?style=for-the-badge)](https://www.uvicorn.org/)
[![HTTPx](https://img.shields.io/badge/HTTPx-Client-5A29E4?style=for-the-badge)](https://www.python-httpx.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063?style=for-the-badge)](https://docs.pydantic.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)](https://github.com)


[Quick Start](#-quick-start) • [Services](#-microservices) • [API Docs](#-api-documentation) • [Documentation](#-documentation) • [Support](#-support)

</div>

---

## 📖 Overview

**School Management System** is a production-ready, enterprise-grade microservices-based platform designed to manage core school operations efficiently. Built with **Python**, **FastAPI**, **Uvicorn (ASGI server)**, **HTTPx (for gateway routing)** and **Pydantic (data validation)**, it provides modular services for handling **students, teachers, classrooms, courses, exams, and attendance**.
Python
This architecture ensures that each core school function is developed, deployed, and scaled independently.

### Key Highlights

The School Management System solves the complexity of managing academic and administrative processes in schools by separating responsibilities into dedicated microservices.



## 🎯 Use Cases

- **Student Information Management** - Maintain student profiles, grades, and enrollment
- **Teacher Management** - Manage teacher profiles, assignments, and teaching records
- **Course Management** - Handle courses, subjects, schedules, and academic structures
- **Classroom Allocation** - Manage classrooms, capacity, and room assignments
- **Exam Management** - Schedule exams, publish results, and track performance
- **Attendance Tracking** - Record and monitor daily student attendance

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 👨‍🎓 Student Management
- Student registration and profile management
- Enrollment into courses and classes
- Academic history tracking
- Guardian/contact information
- Student search and filtering
- Student status management

</td>
<td width="50%">

### 👩‍🏫 Teacher Management
- Teacher onboarding and profile management
- Subject and course assignments
- Qualification and specialization tracking
- Workload and schedule management
- Department associations
- Teacher search and updates

</td>
</tr>
<tr>
<td width="50%">

### 🏫 Classroom & Course Management
- Classroom allocation and capacity management
- Course creation and maintenance
- Subject/course scheduling
- Room assignment for classes
- Academic term and batch management
- Conflict prevention for rooms and schedules

</td>
<td width="50%">

### 📝 Exam & Attendance Management
- Exam scheduling and result publishing
- Marks and grading support
- Daily attendance recording
- Attendance report generation
- Student presence/absence patterns
- Academic performance monitoring

</td>
</tr>
</table>

---

## 🧩 Microservices

The system consists of the following microservices:

### 1. `student_service`
Responsible for managing student-related operations.

**Main Responsibilities**
- Register students
- Update student details
- Maintain guardian/contact info
- Manage student academic records
- Track student enrollment status

---

### 2. `teacher_service`
Responsible for teacher management and academic staff operations.

**Main Responsibilities**
- Register teachers
- Update teacher profiles
- Assign teachers to courses/classes
- Track specialization and department
- Manage teacher status

---

### 3. `classroom_service`
Responsible for classroom and room resource handling.

**Main Responsibilities**
- Create and manage classrooms
- Define seating capacity
- Allocate rooms for classes/exams
- Prevent room conflicts
- Track room usage

---

### 4. `course_service`
Responsible for course and subject management.

**Main Responsibilities**
- Create and manage courses
- Assign subjects
- Manage course schedules
- Map courses to teachers/students
- Handle semester/term-based organization

---

### 5. `exam_service`
Responsible for exam-related processes.

**Main Responsibilities**
- Schedule exams
- Maintain exam records
- Store student marks/results
- Publish exam outcomes
- Support grading logic

---

### 6. `attendance_service`
Responsible for attendance tracking.

**Main Responsibilities**
- Mark daily attendance
- Maintain attendance history
- Generate attendance reports
- Identify absentee patterns
- Support student attendance analytics

---



## 📁 Suggested Project Structure

```bash
school-management-system/
├── api-gateway/
├── service-registry/
├── config-server/
├── attendance_service/
├── classroom_service/
├── course_service/
├── exam_service/
├── student_service/
├── teacher_service/
└── README.md
