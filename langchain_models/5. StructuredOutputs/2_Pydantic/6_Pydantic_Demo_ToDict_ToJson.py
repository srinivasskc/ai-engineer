# pip install pydantic
# pip install pydantic[email]

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import json


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
print(type(student))

# Convert to Dict
student_dict = student.model_dump()
print(student_dict)
print(type(student_dict))
print(student_dict["study"])

# Convert to JSON
student_json = student.model_dump_json()
print(student_json)
print(type(student_json))

# Parse JSON string back to a Python dictionary
data = json.loads(student_json)
print(data)
print(type(data))
print(data["name"])
