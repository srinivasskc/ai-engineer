# Functions.

def create_employee(first,last,pay):
    email = f"{first.lower()}.{last.lower()}@moolya.com"
    return {"first": first, "last" : last, "pay" : pay, "email":  email}


def employee_raise(employee,percentage):
    employee["pay"] = int(employee["pay"] * (1+percentage/100))


empl1 = create_employee("Srinivas", "Kadiyala", 50000)
print(empl1)
employee_raise(empl1,4)
print(empl1)

empl2 = create_employee("Srini", "Kadiyala", 80000)
print(empl2)

