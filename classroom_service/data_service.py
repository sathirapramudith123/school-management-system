from datetime import datetime
from models import Classroom


class ClassroomMockDataService:
    def __init__(self):
        self.classrooms = [
            Classroom(
                id=1,
                room_number="A101",
                building="Main Building",
                capacity=40,
                grade_level=10,
                has_projector=True,
                has_ac=True,
                has_computers=False,
                description="Grade 10 classroom",
                created_at="2024-01-15"
            ),
            Classroom(
                id=2,
                room_number="B201",
                building="Science Block",
                capacity=35,
                grade_level=11,
                has_projector=True,
                has_ac=False,
                has_computers=True,
                description="Physics lab",
                created_at="2024-02-10"
            )
        ]
        self.next_id = 3

    def get_all(self):
        return self.classrooms

    def get_by_id(self, classroom_id: int):
        for classroom in self.classrooms:
            if classroom.id == classroom_id:
                return classroom
        return None

    def get_by_room_number(self, room_number: str):
        for classroom in self.classrooms:
            if classroom.room_number.lower() == room_number.lower():
                return classroom
        return None

    def get_by_building(self, building: str):
        return [
            classroom for classroom in self.classrooms
            if building.lower() in classroom.building.lower()
        ]

    def create(self, classroom_data):
        existing = self.get_by_room_number(classroom_data.room_number)
        if existing:
            return None

        new_classroom = Classroom(
            id=self.next_id,
            room_number=classroom_data.room_number,
            building=classroom_data.building,
            capacity=classroom_data.capacity,
            grade_level=classroom_data.grade_level,
            has_projector=classroom_data.has_projector,
            has_ac=classroom_data.has_ac,
            has_computers=classroom_data.has_computers,
            description=classroom_data.description,
            created_at=datetime.now().strftime("%Y-%m-%d")
        )

        self.classrooms.append(new_classroom)
        self.next_id += 1
        return new_classroom

    def update(self, classroom_id: int, classroom_data):
        classroom = self.get_by_id(classroom_id)
        if not classroom:
            return None

        if classroom_data.room_number is not None:
            existing = self.get_by_room_number(classroom_data.room_number)
            if existing and existing.id != classroom_id:
                return "room_exists"
            classroom.room_number = classroom_data.room_number

        if classroom_data.building is not None:
            classroom.building = classroom_data.building

        if classroom_data.capacity is not None:
            classroom.capacity = classroom_data.capacity

        if classroom_data.grade_level is not None:
            classroom.grade_level = classroom_data.grade_level

        if classroom_data.has_projector is not None:
            classroom.has_projector = classroom_data.has_projector

        if classroom_data.has_ac is not None:
            classroom.has_ac = classroom_data.has_ac

        if classroom_data.has_computers is not None:
            classroom.has_computers = classroom_data.has_computers

        if classroom_data.description is not None:
            classroom.description = classroom_data.description

        return classroom

    def delete(self, classroom_id: int):
        classroom = self.get_by_id(classroom_id)
        if not classroom:
            return False

        self.classrooms.remove(classroom)
        return True