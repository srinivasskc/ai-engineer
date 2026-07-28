# pip install pydantic
# pip install pydantic[email]

from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name: str
    age: int
    study: str = "Langchain"
    school: Optional[str] = None
    email: EmailStr
    cgpa: Optional[float] = Field(
        default=5,
        ge=0,
        le=10,
        description="Decimal Value represents CGPA of student, by default it is None",
    )


new_student = {
    "name": "srinivas",
    "age": 33,
    "school": "SVIT",
    "email": "srinivas@gmail.com",
    "cgpa": 6,
}

student = Student(**new_student)

print(student)


# 1 validation error for Student cgpa
# Input should be less than 10 [type=less_than, input_value=12, input_type=int]
