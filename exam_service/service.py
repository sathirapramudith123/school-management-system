from data_service import ExamMockDataService


class ExamService:
    def __init__(self):
        self.data_service = ExamMockDataService()

    def get_all_exams(self):
        return self.data_service.get_all_exams()

    def get_exam_by_id(self, exam_id: int):
        return self.data_service.get_exam_by_id(exam_id)

    def get_exams_by_course(self, course_id: int):
        return self.data_service.get_exams_by_course(course_id)

    def create_exam(self, exam_data):
        return self.data_service.create_exam(exam_data)

    def update_exam(self, exam_id: int, exam_data):
        return self.data_service.update_exam(exam_id, exam_data)

    def delete_exam(self, exam_id: int):
        return self.data_service.delete_exam(exam_id)

    def get_all_results(self):
        return self.data_service.get_all_results()

    def get_result_by_id(self, result_id: int):
        return self.data_service.get_result_by_id(result_id)

    def get_results_by_exam(self, exam_id: int):
        return self.data_service.get_results_by_exam(exam_id)

    def get_results_by_student(self, student_id: int):
        return self.data_service.get_results_by_student(student_id)

    def create_result(self, result_data):
        return self.data_service.create_result(result_data)

    def update_result(self, result_id: int, result_data):
        return self.data_service.update_result(result_id, result_data)

    def delete_result(self, result_id: int):
        return self.data_service.delete_result(result_id)