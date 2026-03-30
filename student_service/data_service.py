from models import Student
from datetime import datetime


class StudentMockDataService:
    def __init__(self):
        self.students = [
            Student(
                id=1,
                first_name="Kamal",
                last_name="Perera",
                email="kamal.perera@school.com",
                phone="0771234567",
                date_of_birth="2010-05-15",
                grade=10,
                address="Colombo",
                enrolled_date="2024-01-15"
            ),
            Student(
                id=2,
                first_name="Nimal",
                last_name="Silva",
                email="nimal.silva@school.com",
                phone="0787654321",
                date_of_birth="2011-08-22",
                grade=9,
                address="Kandy",
                enrolled_date="2024-01-15"
            )
        ]
        self.next_id = 3

    def get_all(self):
        return self.students

    def get_by_id(self, student_id: int):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def get_by_email(self, email: str):
        for student in self.students:
            if student.email.lower() == email.lower():
                return student
        return None

    def get_by_grade(self, grade: int):
        return [student for student in self.students if student.grade == grade]

    def create(self, student_data):
        existing = self.get_by_email(student_data.email)
        if existing:
            return None

        new_student = Student(
            id=self.next_id,
            first_name=student_data.first_name,
            last_name=student_data.last_name,
            email=student_data.email,
            phone=student_data.phone,
            date_of_birth=student_data.date_of_birth,
            grade=student_data.grade,
            address=student_data.address,
            enrolled_date=datetime.now().strftime("%Y-%m-%d")
        )

        self.students.append(new_student)
        self.next_id += 1
        return new_student

    def update(self, student_id: int, student_data):
        student = self.get_by_id(student_id)
        if not student:
            return None

        if student_data.first_name is not None:
            student.first_name = student_data.first_name

        if student_data.last_name is not None:
            student.last_name = student_data.last_name

        if student_data.email is not None:
            existing = self.get_by_email(student_data.email)
            if existing and existing.id != student_id:
                return "email_exists"
            student.email = student_data.email

        if student_data.phone is not None:
            student.phone = student_data.phone

        if student_data.grade is not None:
            student.grade = student_data.grade

        if student_data.address is not None:
            student.address = student_data.address

        return student

    def delete(self, student_id: int):
        student = self.get_by_id(student_id)
        if not student:
            return False

        self.students.remove(student)
        return True