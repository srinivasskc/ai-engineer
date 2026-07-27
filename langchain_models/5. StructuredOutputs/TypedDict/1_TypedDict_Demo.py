# TypedDict - To define a python dictionary in python,to specificy what keys and values should exists.
# It helps to ensure dictionary follows specific structure.
# It tells python, what keys are required and what type of values it should have.
# It does not validate data at runtime.

from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


new_person: Person = {"name": "Srinivas", "age": "32"}

print(new_person)
