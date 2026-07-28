# pip install pydantic

from pydantic import BaseModel


# name is defined as string
class Student(BaseModel):
    name: str
    age: int


# But in dictionary, value is int.
new_student = {"name": 33, "age": 33}

# ** is for dictionary unpacking operator.
# unpacks key-value pairs from a dictionary into keyword arguments.
student = Student(**new_student)

print(student)
print(type(student))

print(student.name)
print(student.age)


"""
pydantic_core._pydantic_core.ValidationError: 1 validation error for Student name
Input should be a valid string [type=string_type, input_value=33, input_type=int]
"""
