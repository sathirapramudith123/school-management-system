from models import Attendance
from datetime import datetime, date


class AttendanceMockDataService:
    def __init__(self):
        today = date.today().isoformat()

        self.attendance_records = [
            Attendance(
                id=1,
                student_id=1,
                course_id=101,
                date=today,
                status="present",
                marked_by=1,
                remarks="On time",
                marked_at=datetime.now().isoformat()
            ),
            Attendance(
                id=2,
                student_id=2,
                course_id=101,
                date=today,
                status="absent",
                marked_by=1,
                remarks="Sick leave",
                marked_at=datetime.now().isoformat()
            )
        ]
        self.next_id = 3

    def get_all(self):
        return self.attendance_records

    def get_by_id(self, attendance_id: int):
        for record in self.attendance_records:
            if record.id == attendance_id:
                return record
        return None

    def get_by_student(self, student_id: int):
        return [r for r in self.attendance_records if r.student_id == student_id]

    def get_by_course(self, course_id: int):
        return [r for r in self.attendance_records if r.course_id == course_id]

    def create(self, attendance_data):
        if not attendance_data.date:
            attendance_data.date = date.today().isoformat()

        for record in self.attendance_records:
            if (
                record.student_id == attendance_data.student_id
                and record.course_id == attendance_data.course_id
                and record.date == attendance_data.date
            ):
                return None

        new_record = Attendance(
            id=self.next_id,
            student_id=attendance_data.student_id,
            course_id=attendance_data.course_id,
            date=attendance_data.date,
            status=attendance_data.status,
            marked_by=attendance_data.marked_by,
            remarks=attendance_data.remarks,
            marked_at=datetime.now().isoformat()
        )

        self.attendance_records.append(new_record)
        self.next_id += 1
        return new_record

    def update(self, attendance_id: int, attendance_data):
        record = self.get_by_id(attendance_id)
        if not record:
            return None

        if attendance_data.status is not None:
            record.status = attendance_data.status

        if attendance_data.remarks is not None:
            record.remarks = attendance_data.remarks

        return record

    def delete(self, attendance_id: int):
        record = self.get_by_id(attendance_id)
        if not record:
            return False

        self.attendance_records.remove(record)
        return True