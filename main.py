from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
import services
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/courses", response_model=schemas.CourseBase)
def create_course(course: schemas.CourseBase, db: Session = Depends(get_db)):
    db_course = services.get_course_by_name(db, course.name)
    if db_course:
        raise HTTPException(status_code=400, detail="Course with the same name already exists")
    return services.create_course(db, course)


@app.get("/courses/{id}", response_model=schemas.CourseBase)
def get_course(id: int, db: Session = Depends(get_db)):
    print('da')
    return services.get_course(db, id)


@app.get("/courses", response_model=List[schemas.CourseBase])
def get_courses(db: Session = Depends(get_db)):
    return services.get_courses(db)


@app.put("/courses/{id}", response_model=schemas.CourseBase)
def update_course(course: schemas.CourseBase, id:int, db: Session = Depends(get_db)):
    return services.update_course(db, id, course)


@app.delete("/courses/{id}", response_model=schemas.CourseBase)
def delete_course_by_id(id: int, db: Session = Depends(get_db)):
    return services.delete_course(db, id)


@app.get("/courses/enrolled/{id}", response_model=List[schemas.StudentBase])
def get_enrolled_students(id: int, db: Session = Depends(get_db)):
    return services.get_enrolled(db, id)


# Students


@app.post("/student", response_model=schemas.StudentBase)
def create_student(student: schemas.StudentBase, db: Session = Depends(get_db)):
    check_student = services.student_exists(db, student.name, student.surname, student.course_id)
    if check_student:
        raise HTTPException(status_code=400, detail="Student with same credentials already exists")
    return services.create_student(db, student)


@app.get("/students/{id}", response_model=schemas.StudentBase)
def get_student(id: int, db: Session = Depends(get_db)):
    return services.get_student(db, id)


@app.get("/students", response_model=List[schemas.StudentBase])
def get_students(db: Session = Depends(get_db)):
    return services.get_students(db)


@app.put("/students/{id}", response_model=schemas.StudentBase)
def update_student(student: schemas.StudentBase, id:int, db: Session = Depends(get_db)):
    return services.update_student(db, id, student)


@app.delete("/student/{id}", response_model=schemas.StudentBase)
def delete_student(id: int, db: Session = Depends(get_db)):
    return services.delete_student(db, id)





