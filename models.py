from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Course(Base):
    __tablename__ = "course"

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __init__(self,id, name, level):
        self.id = id
        self.name = name
        self.level = level


    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    level = Column(Integer)

    students = relationship("Student", back_populates="course")


class Student(Base):
    __tablename__ = "students"

    def __init__(self, id, name, surname, course_id):
        self.id = id
        self.name = name
        self.surname = surname
        self.course_id = course_id

    def __init__(self, name, surname, course_id):
        self.name = name
        self.surname = surname
        self.course_id = course_id

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    course_id = Column(Integer, ForeignKey("course.id"))

    course = relationship("Course", back_populates="students")