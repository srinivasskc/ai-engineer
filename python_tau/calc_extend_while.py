on = True


def add():
    a = float(input("Enter the number: "))
    b = float(input("Enter another number: "))
    print("Addition -> a+b: ", a + b)


def subtract():
    a = float(input("Enter the number: "))
    b = float(input("Enter another number: "))
    print("Subtract -> a-b: ", a - b)


def multiply():
    a = float(input("Enter the number: "))
    b = float(input("Enter another number: "))
    print("Multiply ->  a*b: ", a * b)


def divide():
    a = float(input("Enter the number: "))
    b = float(input("Enter another number: "))
    print("Division ->  a/b: ", a / b)


while on:
    operation = input("Please type: +, - , * , /, or q: ").strip().lower()
    if operation == "+":
        add()
    elif operation == "-":
        subtract()
    elif operation == "*":
        multiply()
    elif operation == "/":
        divide()
    elif operation == "q":
        on = False
    else:
        print("Operator not found. Please try again!")
