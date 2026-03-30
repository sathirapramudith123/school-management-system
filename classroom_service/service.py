from data_service import ClassroomMockDataService


class ClassroomService:
    def __init__(self):
        self.data_service = ClassroomMockDataService()

    def get_all_classrooms(self):
        return self.data_service.get_all()

    def get_classroom_by_id(self, classroom_id: int):
        return self.data_service.get_by_id(classroom_id)

    def get_classroom_by_room_number(self, room_number: str):
        return self.data_service.get_by_room_number(room_number)

    def get_classrooms_by_building(self, building: str):
        return self.data_service.get_by_building(building)

    def create_classroom(self, classroom_data):
        return self.data_service.create(classroom_data)

    def update_classroom(self, classroom_id: int, classroom_data):
        return self.data_service.update(classroom_id, classroom_data)

    def delete_classroom(self, classroom_id: int):
        return self.data_service.delete(classroom_id)