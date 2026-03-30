from data_service import TeacherMockDataService


class TeacherService:
    def __init__(self):
        self.data_service = TeacherMockDataService()

    def get_all_teachers(self):
        return self.data_service.get_all()

    def get_teacher_by_id(self, teacher_id: int):
        return self.data_service.get_by_id(teacher_id)

    def get_teacher_by_email(self, email: str):
        return self.data_service.get_by_email(email)

    def get_teachers_by_specialization(self, specialization: str):
        return self.data_service.get_by_specialization(specialization)

    def create_teacher(self, teacher_data):
        return self.data_service.create(teacher_data)

    def update_teacher(self, teacher_id: int, teacher_data):
        return self.data_service.update(teacher_id, teacher_data)

    def delete_teacher(self, teacher_id: int):
        return self.data_service.delete(teacher_id)