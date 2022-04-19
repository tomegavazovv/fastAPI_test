from sqlalchemy.orm import Session
import models, schemas

# Courses

def get_courses(db:Session):
    return db.query(models.Course).all()

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def get_course_by_name(db: Session, course_name: str):
    return db.query(models.Course).filter(models.Course.name == course_name).first()

def create_course(db: Session, course: schemas.CourseBase):
    coursedb = models.Course(course.name, course.level)
    db.add(coursedb)
    db.commit()
    return coursedb

def update_course(db:Session, id: int, course: schemas.CourseBase):
    to_update = db.query(models.Course).filter(models.Course.id == id).first()
    to_update.name = course.name
    to_update.level = course.level
    db.commit()
    db.flush()
    return to_update

def delete_course(db:Session, course_id: int):
    to_delete = db.query(models.Course).filter(models.Course.id == course_id).first()
    db.delete(to_delete)
    db.commit()
    return to_delete

def get_enrolled(db:Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first().students


# Students

def get_students(db:Session):
    return db.query(models.Student).all()

def student_exists(db:Session, name, surname, course_id):
    return db.query(models.Student).filter(models.Student.name == name and
                                           models.Student.surname == surname and
                                           models.Student.course_id == course_id).first()

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def create_student(db: Session, student: schemas.StudentBase):
    studentdb = models.Student(student.name, student.surname, student.course_id)
    db.add(studentdb)
    db.commit()
    return student

def update_student(db:Session, id: int, student: schemas.StudentBase):
    to_update = db.query(models.Student).filter(models.Student.id == id).first()
    to_update.name = student.name
    to_update.surname = student.surname
    to_update.course_id = student.course_id
    db.commit()
    db.flush()
    return to_update

def delete_student(db:Session, student_id: int):
    to_delete = db.query(models.Student).filter(models.Student.id == student_id).first()
    db.delete(to_delete)
    db.commit()
    return to_delete


