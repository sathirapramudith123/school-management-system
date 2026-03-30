from models import Exam, ExamResult


class ExamMockDataService:
    def __init__(self):
        self.exams = [
            Exam(
                id=1,
                name="Math Midterm",
                course_id=101,
                exam_date="2026-04-15",
                duration_minutes=120,
                total_marks=100,
                passing_marks=35,
                exam_type="midterm"
            ),
            Exam(
                id=2,
                name="Physics Final",
                course_id=102,
                exam_date="2026-05-20",
                duration_minutes=180,
                total_marks=100,
                passing_marks=40,
                exam_type="final"
            )
        ]

        self.results = [
            ExamResult(
                id=1,
                exam_id=1,
                student_id=1,
                marks_obtained=78,
                grade="A",
                remarks="Good job"
            ),
            ExamResult(
                id=2,
                exam_id=1,
                student_id=2,
                marks_obtained=52,
                grade="C",
                remarks="Needs improvement"
            )
        ]

        self.next_exam_id = 3
        self.next_result_id = 3

    # ---------- Exam Methods ----------

    def get_all_exams(self):
        return self.exams

    def get_exam_by_id(self, exam_id: int):
        for exam in self.exams:
            if exam.id == exam_id:
                return exam
        return None

    def get_exams_by_course(self, course_id: int):
        return [exam for exam in self.exams if exam.course_id == course_id]

    def create_exam(self, exam_data):
        new_exam = Exam(
            id=self.next_exam_id,
            name=exam_data.name,
            course_id=exam_data.course_id,
            exam_date=exam_data.exam_date,
            duration_minutes=exam_data.duration_minutes,
            total_marks=exam_data.total_marks,
            passing_marks=exam_data.passing_marks,
            exam_type=exam_data.exam_type
        )
        self.exams.append(new_exam)
        self.next_exam_id += 1
        return new_exam

    def update_exam(self, exam_id: int, exam_data):
        exam = self.get_exam_by_id(exam_id)
        if not exam:
            return None

        if exam_data.name is not None:
            exam.name = exam_data.name
        if exam_data.exam_date is not None:
            exam.exam_date = exam_data.exam_date
        if exam_data.duration_minutes is not None:
            exam.duration_minutes = exam_data.duration_minutes
        if exam_data.total_marks is not None:
            exam.total_marks = exam_data.total_marks
        if exam_data.passing_marks is not None:
            exam.passing_marks = exam_data.passing_marks
        if exam_data.exam_type is not None:
            exam.exam_type = exam_data.exam_type

        return exam

    def delete_exam(self, exam_id: int):
        exam = self.get_exam_by_id(exam_id)
        if not exam:
            return False

        self.exams.remove(exam)
        self.results = [r for r in self.results if r.exam_id != exam_id]
        return True

    # ---------- Result Methods ----------

    def calculate_grade(self, marks_obtained: float, total_marks: int):
        percentage = (marks_obtained / total_marks) * 100

        if percentage >= 75:
            return "A"
        elif percentage >= 65:
            return "B"
        elif percentage >= 55:
            return "C"
        elif percentage >= 40:
            return "S"
        else:
            return "F"

    def get_all_results(self):
        return self.results

    def get_result_by_id(self, result_id: int):
        for result in self.results:
            if result.id == result_id:
                return result
        return None

    def get_results_by_exam(self, exam_id: int):
        return [result for result in self.results if result.exam_id == exam_id]

    def get_results_by_student(self, student_id: int):
        return [result for result in self.results if result.student_id == student_id]

    def create_result(self, result_data):
        exam = self.get_exam_by_id(result_data.exam_id)
        if not exam:
            return None

        grade = self.calculate_grade(result_data.marks_obtained, exam.total_marks)

        new_result = ExamResult(
            id=self.next_result_id,
            exam_id=result_data.exam_id,
            student_id=result_data.student_id,
            marks_obtained=result_data.marks_obtained,
            grade=grade,
            remarks=result_data.remarks
        )

        self.results.append(new_result)
        self.next_result_id += 1
        return new_result

    def update_result(self, result_id: int, result_data):
        result = self.get_result_by_id(result_id)
        if not result:
            return None

        exam = self.get_exam_by_id(result.exam_id)

        if result_data.marks_obtained is not None:
            result.marks_obtained = result_data.marks_obtained
            result.grade = self.calculate_grade(result.marks_obtained, exam.total_marks)

        if result_data.remarks is not None:
            result.remarks = result_data.remarks

        return result

    def delete_result(self, result_id: int):
        result = self.get_result_by_id(result_id)
        if not result:
            return False

        self.results.remove(result)
        return True