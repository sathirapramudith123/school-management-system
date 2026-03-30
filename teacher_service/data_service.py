from models import Teacher
from datetime import datetime


class TeacherMockDataService:
    def __init__(self):
        self.teachers = [
            Teacher(
                id=1,
                first_name="Priyanka",
                last_name="Wijesinghe",
                email="priyanka.wijesinghe@school.com",
                phone="0771112233",
                specialization="Mathematics",
                qualification="BSc in Mathematics",
                address="Colombo",
                joined_date="2020-01-15",
                salary=75000.0
            ),
            Teacher(
                id=2,
                first_name="Saman",
                last_name="Jayasuriya",
                email="saman.jayasuriya@school.com",
                phone="0784445566",
                specialization="Physics",
                qualification="BSc in Physics",
                address="Kandy",
                joined_date="2019-06-10",
                salary=72000.0
            )
        ]
        self.next_id = 3

    def get_all(self):
        return self.teachers

    def get_by_id(self, teacher_id: int):
        for teacher in self.teachers:
            if teacher.id == teacher_id:
                return teacher
        return None

    def get_by_email(self, email: str):
        for teacher in self.teachers:
            if teacher.email.lower() == email.lower():
                return teacher
        return None

    def get_by_specialization(self, specialization: str):
        return [
            teacher for teacher in self.teachers
            if teacher.specialization.lower() == specialization.lower()
        ]

    def create(self, teacher_data):
        existing = self.get_by_email(teacher_data.email)
        if existing:
            return None

        new_teacher = Teacher(
            id=self.next_id,
            first_name=teacher_data.first_name,
            last_name=teacher_data.last_name,
            email=teacher_data.email,
            phone=teacher_data.phone,
            specialization=teacher_data.specialization,
            qualification=teacher_data.qualification,
            address=teacher_data.address,
            joined_date=datetime.now().strftime("%Y-%m-%d"),
            salary=teacher_data.salary
        )

        self.teachers.append(new_teacher)
        self.next_id += 1
        return new_teacher

    def update(self, teacher_id: int, teacher_data):
        teacher = self.get_by_id(teacher_id)
        if not teacher:
            return None

        if teacher_data.first_name is not None:
            teacher.first_name = teacher_data.first_name

        if teacher_data.last_name is not None:
            teacher.last_name = teacher_data.last_name

        if teacher_data.email is not None:
            existing = self.get_by_email(teacher_data.email)
            if existing and existing.id != teacher_id:
                return "email_exists"
            teacher.email = teacher_data.email

        if teacher_data.phone is not None:
            teacher.phone = teacher_data.phone

        if teacher_data.specialization is not None:
            teacher.specialization = teacher_data.specialization

        if teacher_data.qualification is not None:
            teacher.qualification = teacher_data.qualification

        if teacher_data.address is not None:
            teacher.address = teacher_data.address

        if teacher_data.salary is not None:
            teacher.salary = teacher_data.salary

        return teacher

    def delete(self, teacher_id: int):
        teacher = self.get_by_id(teacher_id)
        if not teacher:
            return False

        self.teachers.remove(teacher)
        return True