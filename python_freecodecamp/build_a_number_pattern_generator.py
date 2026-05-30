def number_pattern(n):
    # 1. Check if the argument is an integer
    if type(n) is not int:
        return "Argument must be an integer value."

    # 2. Check if the integer is greater than 0
    if n < 1:
        return "Argument must be an integer greater than 0."

    # 3. Use a for loop to generate the numbers
    numbers = []
    for i in range(1, n + 1):
        numbers.append(str(i))

    # 4. Return the space-separated string
    return " ".join(numbers)


result_4 = number_pattern(4)
print("number: ", result_4)

result_12 = number_pattern(12)
print("number: ", result_12)
