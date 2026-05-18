# Class Variable

class Employee:

    # Class Variables
    raise_percentage = 1.04
    count = 0

    # instance variables
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay  = pay
        self.email = f"{first.lower()}.{last.lower()}@moolya.com"
        Employee.count += 1

    def employee_fullname(self):
        return f"{self.first} {self.last}"
    
    def increase_pay(self):
        self.pay = int(self.pay * self.raise_percentage) 

emp1 = Employee("Srinivas","Kadiyala", 50000)
emp2 = Employee("Srini","Kadiyala", 80000)


print(emp1.raise_percentage)
print(emp2.raise_percentage)
print(Employee.raise_percentage)

print(emp1.pay)
emp1.increase_pay()
print(emp1.pay)

# dict
print(emp1.__dict__)
print("\n")
print(Employee.__dict__)

# Changing the raise percentage value
print("\n")
Employee.raise_percentage = 1.07

print(Employee.raise_percentage)
# This prints new value

print(emp1.raise_percentage)
# This prints new value

emp1.raise_percentage = 1.10
print(emp1.raise_percentage)
# This prints new value at individual level.

print(emp2.raise_percentage)
# This prints value at Global level.

print("Employee Count: ",Employee.count)
