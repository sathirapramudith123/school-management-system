from data_service import StudentMockDataService


class StudentService:
    def __init__(self):
        self.data_service = StudentMockDataService()

    def get_all_students(self):
        return self.data_service.get_all()

    def get_student_by_id(self, student_id: int):
        return self.data_service.get_by_id(student_id)

    def get_student_by_email(self, email: str):
        return self.data_service.get_by_email(email)

    def get_students_by_grade(self, grade: int):
        return self.data_service.get_by_grade(grade)

    def create_student(self, student_data):
        return self.data_service.create(student_data)

    def update_student(self, student_id: int, student_data):
        return self.data_service.update(student_id, student_data)

    def delete_student(self, student_id: int):
        return self.data_service.delete(student_id)