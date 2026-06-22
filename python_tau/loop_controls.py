print("====Break====")

temp_f = 101

while temp_f > 98:
    print(f"Have {temp_f} degrees temperature, Having Fever")
    temp_f -= 1
    if temp_f == 99:
        break
print(f"Now Temperature is {temp_f} degress, It's Normal now")


print("\n ====Continue=====")

for number in range(1, 11):
    if number == 7:
        print("Skipping the number 7")
        continue
    print(f"Number is {number}")


print("\n ====PASS=====")

for number in range(1, 11):
    if number == 3:
        pass
    else:
        print(f"Number is {number}")
