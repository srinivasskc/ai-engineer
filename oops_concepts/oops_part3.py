class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay  = pay
        self.email = f"{first.lower()}.{last.lower()}@moolya.com"

    def employee_fullname(self):
        return f"{self.first} {self.last}"
    
    def increase_pay(self, percentage):
        self.pay = int(self.pay * (1+percentage/100))


emp1 = Employee("Srinivas","Kadiyala", 50000)

# Each instance has its own data
print(emp1)
print(emp1.first)
print(emp1.last)
print(emp1.pay)
print(emp1.email)


emp2 = Employee("Srini","Kadiyala", 10000)

# Each instance has its own data
print(emp2)
print(emp2.first)
print(emp2.last)
print(emp2.pay)
print(emp2.email)


# Changing the employee value of Employee 1 only.
emp1.pay = 85000
print(emp1)
print(emp1.pay)
print(emp2.pay)

# Using __dict__ printing the employee details
print(emp1.__dict__)
# We can see the latest pay is updated


# Calling employee_fullname()
print("Employee Full_Name: ",emp1.employee_fullname())
print("Employee Full_Name: ",emp2.employee_fullname())

# Calling increase_pay
print(emp1.pay)   # Initial Value
emp1.increase_pay(4)
print(emp1.pay)   # After increase Value
print(emp1.__dict__)


# Another way to call methods.
print(emp2.__dict__)
print(emp2.pay)
Employee.increase_pay(emp2,5)
print(emp2.pay)