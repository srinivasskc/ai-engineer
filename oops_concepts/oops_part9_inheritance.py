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
    pass

dev1 = Developer("Arjun","Tendulkar",20000)  #Instance of Developer Class
emp1 = Employee("Srini","Kadiyala",10000)  #Instance of Employee Class

print(dev1.employee_fullname()) #inherited
print(dev1.first) #inherited
print(dev1.last)  #inherited
print(dev1.email) #inherited

print(dev1.pay) #inherited
dev1.increase_pay() #inherited
print(dev1.pay) #inherited

print(Developer.raise_percentage)
print(Developer.number_of_employees)





















# Inheriting the Employee information to Manager
class Manager(Employee):
    pass
