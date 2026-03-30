from fastapi import FastAPI, HTTPException, status
from typing import List
from models import Classroom, ClassroomCreate, ClassroomUpdate
from service import ClassroomService

app = FastAPI(
    title="Classroom Microservice",
    version="1.0.0"
)

classroom_service = ClassroomService()


@app.get("/")
def root():
    return {"message": "Classroom Microservice is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/classrooms", response_model=List[Classroom])
def get_all_classrooms():
    return classroom_service.get_all_classrooms()


@app.get("/classrooms/room/{room_number}", response_model=Classroom)
def get_classroom_by_room_number(room_number: str):
    classroom = classroom_service.get_classroom_by_room_number(room_number)
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return classroom


@app.get("/classrooms/building/{building}", response_model=List[Classroom])
def get_classrooms_by_building(building: str):
    return classroom_service.get_classrooms_by_building(building)


@app.get("/classrooms/{classroom_id}", response_model=Classroom)
def get_classroom(classroom_id: int):
    classroom = classroom_service.get_classroom_by_id(classroom_id)
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return classroom


@app.post("/classrooms", response_model=Classroom, status_code=status.HTTP_201_CREATED)
def create_classroom(classroom: ClassroomCreate):
    if classroom.capacity <= 0:
        raise HTTPException(status_code=400, detail="Capacity must be greater than 0")

    if classroom.grade_level is not None and (classroom.grade_level < 1 or classroom.grade_level > 13):
        raise HTTPException(status_code=400, detail="Grade level must be between 1 and 13")

    new_classroom = classroom_service.create_classroom(classroom)
    if not new_classroom:
        raise HTTPException(status_code=400, detail="Room number already exists")

    return new_classroom


@app.put("/classrooms/{classroom_id}", response_model=Classroom)
def update_classroom(classroom_id: int, classroom: ClassroomUpdate):
    if classroom.capacity is not None and classroom.capacity <= 0:
        raise HTTPException(status_code=400, detail="Capacity must be greater than 0")

    if classroom.grade_level is not None and (classroom.grade_level < 1 or classroom.grade_level > 13):
        raise HTTPException(status_code=400, detail="Grade level must be between 1 and 13")

    updated_classroom = classroom_service.update_classroom(classroom_id, classroom)

    if updated_classroom is None:
        raise HTTPException(status_code=404, detail="Classroom not found")

    if updated_classroom == "room_exists":
        raise HTTPException(status_code=400, detail="Room number already exists")

    return updated_classroom


@app.delete("/classrooms/{classroom_id}")
def delete_classroom(classroom_id: int):
    success = classroom_service.delete_classroom(classroom_id)
    if not success:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return {"message": "Classroom deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=True)