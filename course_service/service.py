from data_service import CourseMockDataService


class CourseService:
    def __init__(self):
        self.data_service = CourseMockDataService()

    def get_all_courses(self):
        return self.data_service.get_all()

    def get_course_by_id(self, course_id: int):
        return self.data_service.get_by_id(course_id)

    def get_course_by_code(self, code: str):
        return self.data_service.get_by_code(code)

    def create_course(self, course_data):
        return self.data_service.create(course_data)

    def update_course(self, course_id: int, course_data):
        return self.data_service.update(course_id, course_data)

    def delete_course(self, course_id: int):
        return self.data_service.delete(course_id)