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


# Inheriting the Employee information to Developer
class Developer(Employee):
    # Overriding the raise_percentage from Class Employee.
    raise_percentage = 1.10  #Increased from 1.04 to 1.10

    # Adding extra variables to Developer class using super().__init__
    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang   #New Variable.


dev1 = Developer("Arjun","Tendulkar",20000,"Python")  #Instance of Developer  with Prog_lang
emp1 = Employee("Srini","Kadiyala",10000)  #Instance of Employee Class

print("====Developer=====")
print(dev1.first)
print(dev1.last)
print(dev1.pay)
print(dev1.prog_lang)

print(dev1.pay) #inherited
dev1.increase_pay() #inherited
print(dev1.pay) #inherited
print(Developer.raise_percentage)

print("====Employee=====")
print(emp1.pay) #inherited
emp1.increase_pay() #inherited
print(emp1.pay) #inherited
print(Employee.raise_percentage)

# Inheriting the Employee information to Manager

"""
Encapsulation:

Whenever a manager gets a raise, every developer gets a small bonus too.
"""


class Manager(Employee):
    # Manager raise_percentage.
    raise_percentage = 2.00

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employees(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_employees(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(f" Employee --> {emp.employee_fullname()}")

    def increase_pay(self):
        super().increase_pay()   #do what employee gets.
        for emp in self.employees:
            emp.pay = int(emp.pay * 1.01)

dev1 = Developer("Arjun","Tendulkar",20000,"Python")
dev2 = Developer("Sara","Tendulkar",24000,"Java")

mgr1 = Manager("Sachin","Tendulkar",150000,[dev1])

mgr1.print_employees()
mgr1.add_employees(dev2)
print("===After adding Employee===")
mgr1.print_employees()
print("===Removing the first Empoyee===")
mgr1.remove_employees(dev1)
mgr1.print_employees()

print("===Before changes pay===")
print(f"Manager: Rs.{mgr1.pay: }")
print(f" {dev1.first}: Rs.{dev1.pay: }")
print(f" {dev2.first}: Rs.{dev2.pay: }")

mgr1.increase_pay()
print("===After changes pay===")
print(f"Manager: Rs.{mgr1.pay: }")
print(f" {dev1.first}: Rs.{dev1.pay: }")
print(f" {dev2.first}: Rs.{dev2.pay: }")

