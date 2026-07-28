# pip install pydantic
# pip install pydantic[email]

from pydantic import BaseModel, EmailStr
from typing import Optional


class Student(BaseModel):
    name: str
    age: int
    study: str = "Langchain"
    school: Optional[str] = None
    email: EmailStr


new_student = {"name": "srinivas", "age": 33, "school": "SVIT", "email": "srinivas"}

student = Student(**new_student)

print(student)


# value is not a valid email address: An email address must have an @-sign. [type=value_error, input_value='srinivas', # input_type=str]
