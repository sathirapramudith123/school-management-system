from models import Course


class CourseMockDataService:
    def __init__(self):
        self.courses = [
            Course(id=1, name="Computer Science", code="CS101", credits=3),
            Course(id=2, name="Information Technology", code="IT201", credits=4),
            Course(id=3, name="Data Science", code="DS301", credits=3)
        ]
        self.next_id = 4

    def get_all(self):
        return self.courses

    def get_by_id(self, course_id: int):
        for course in self.courses:
            if course.id == course_id:
                return course
        return None

    def get_by_code(self, code: str):
        for course in self.courses:
            if course.code.lower() == code.lower():
                return course
        return None

    def create(self, course_data):
        existing = self.get_by_code(course_data.code)
        if existing:
            return None

        new_course = Course(
            id=self.next_id,
            name=course_data.name,
            code=course_data.code,
            credits=course_data.credits
        )

        self.courses.append(new_course)
        self.next_id += 1
        return new_course

    def update(self, course_id: int, course_data):
        course = self.get_by_id(course_id)
        if not course:
            return None

        if course_data.name is not None:
            course.name = course_data.name

        if course_data.code is not None:
            existing = self.get_by_code(course_data.code)
            if existing and existing.id != course_id:
                return "code_exists"
            course.code = course_data.code

        if course_data.credits is not None:
            course.credits = course_data.credits

        return course

    def delete(self, course_id: int):
        course = self.get_by_id(course_id)
        if not course:
            return False

        self.courses.remove(course)
        return True