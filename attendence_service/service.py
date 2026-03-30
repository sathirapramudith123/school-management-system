from data_service import AttendanceMockDataService


class AttendanceService:
    def __init__(self):
        self.data_service = AttendanceMockDataService()

    def get_all_attendance(self):
        return self.data_service.get_all()

    def get_attendance_by_id(self, attendance_id: int):
        return self.data_service.get_by_id(attendance_id)

    def get_attendance_by_student(self, student_id: int):
        return self.data_service.get_by_student(student_id)

    def get_attendance_by_course(self, course_id: int):
        return self.data_service.get_by_course(course_id)

    def create_attendance(self, attendance_data):
        return self.data_service.create(attendance_data)

    def update_attendance(self, attendance_id: int, attendance_data):
        return self.data_service.update(attendance_id, attendance_data)

    def delete_attendance(self, attendance_id: int):
        return self.data_service.delete(attendance_id)