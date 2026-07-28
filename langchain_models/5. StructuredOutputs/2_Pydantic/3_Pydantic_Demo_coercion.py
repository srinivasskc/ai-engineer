# pip install pydantic

from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    name: str
    age: int
    study: str = "Langchain"  # Setting default value
    school: Optional[str] = None  # if in dictionary, value is not provided


# Pydantic Type coercion (data parsing - age: str to int)
new_student = {"name": "srinivas", "age": "33", "school": "SVIT"}


# ** is for dictionary unpacking operator.
# unpacks key-value pairs from a dictionary into keyword arguments.
student = Student(**new_student)

print(student)
print(type(student))

print(student.name)
print(student.age)
print(student.study)
print(student.school)

print(type(student.age))
