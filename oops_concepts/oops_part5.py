# With Slots

class Employee:

    __slots__ = ["first","last","pay","email"]
    # This will enforce python.

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay  = pay
        self.email = f"{first.lower()}.{last.lower()}@moolya.com"

    def employee_fullname(self):
        return f"{self.first} {self.last}"
    
    def increase_pay(self, percentage):
        self.pay = int(self.pay * 1.04) # 4 percent


emp1 = Employee("Srinivas","Kadiyala", 50000)

print(emp1.__dict__)

# emp1.pya = 90000  # Typo
print(emp1.__dict__) #Now error is thrown, as __dict__ is not part of slots attribute.