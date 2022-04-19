from typing import List, Optional
from pydantic import BaseModel, Field


class CourseBase(BaseModel):
    name: str = Field(..., min_length=3)
    level: int = Field(..., gt=0, le=3)

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str = Field(..., min_length=3)
    surname: str = Field(..., min_length=3)
    course_id: int

    class Config:
        orm_mode = True
