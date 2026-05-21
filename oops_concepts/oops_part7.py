# Class Variable

class Employee:

    # Class Variables
    raise_percentage = 1.04
    number_of_employees = 0
    company = "Moolya"

    # instance variables
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay  = pay
        self.email = f"{first.lower()}.{last.lower()}@{Employee.company.lower()}.com"
        Employee.number_of_employees += 1

    def employee_fullname(self):
        return f"{self.first} {self.last}"
    
    def increase_pay(self):
        self.pay = int(self.pay * self.raise_percentage) 

    
    # ClassMethods: Method whose first parameter is cls, not self.
    
    @classmethod
    def set_raise_percentage(cls, amount):
        cls.raise_percentage=amount

    @classmethod
    def get_count(cls):
        return cls.number_of_employees
    
    @staticmethod
    def is_workday(day):
        return day.weekday() < 5    #M-0,T-1,W-2,TH-3,F-4,S-5,SU-6


# Fetching the Class Variable without calling an instance of class
print(Employee.raise_percentage)  #1.04

# Setting new value.
Employee.set_raise_percentage(1.07)   #No Instance variable required
print(Employee.raise_percentage)   #Changes the value from 1.04 to 1.07


# Print No of Employees
print("No of Employees=",Employee.get_count())  # Initial value - 0

# Creating instances of class.
emp1 = Employee("Srini","Kadiyala",50000)
emp2 = Employee("Srinivas","K",35000)

Employee.set_raise_percentage(1.10)   #Change to 1.10 from 1.07
print(emp1.raise_percentage)
print(emp2.raise_percentage)

# Print No of Employees after initialization.
print("No of Employees=",Employee.get_count())  # Value - 2


# Getting the is workday or not, with static method.
import datetime

my_date = datetime.date(2026,5,21) #Thu-True
print(Employee.is_workday(my_date))

my_date = datetime.date(2026,5,23)  #Sat-False
print(Employee.is_workday(my_date))
