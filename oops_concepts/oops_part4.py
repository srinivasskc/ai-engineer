class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay  = pay
        self.email = f"{first.lower()}.{last.lower()}@moolya.com"

    def employee_fullname(self):
        return f"{self.first} {self.last}"
    
    def increase_pay(self, percentage):
        self.pay = int(self.pay * 1.04)


emp1 = Employee("Srinivas","Kadiyala", 50000)

print(emp1.__dict__)

emp1.pya = 90000  # Typo
print(emp1.__dict__) #Pay is still original value, but with new value.


# If we are adding a new attribute for employee instance 0, but not added for 1st.
# It will throw an error: tuple object has no attribute "department"
# To solve, we will add __slots__

employees = [Employee("Srinivas", "Kadiyala", 80000),
                ("Srini","Kadiyala", 90000)]

employees[0].department = "Engineering"

for emp in employees:
    print(emp.department)


             