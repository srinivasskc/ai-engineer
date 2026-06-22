fruits = ["Banana", "Apple", "Cherry"]
years = [30, "1990", 1, 3.0]

print(f"Fruits: {fruits}")
print(f"Years: {years}")

# Adding item to list
fruits.append("Orange")
print(f"Fruits: {fruits}")

# Extending list with another list
fruits.extend(years)
print(f"Fruits: {fruits}")

# Remove Item from list
fruits.remove("Orange")
print(f"Fruits: {fruits}")

# Remove Item from list using Index
fruits.pop(0)
print(f"Fruits: {fruits}")

fruits.pop(-1)
print(f"Fruits: {fruits}")

# Sort the List with same datatype items
numbers = [1, 11, 2, 22, 3, 33, 4, 44, 5, 55]
numbers.sort()
print(numbers)

numbers.append(6.0)
print(numbers)

numbers.sort()
print(numbers)

# Membership = Check if item exists in list - Returns True or False
print("Apple" in fruits)
print("apple" in fruits)

# Count of Item in the list
print(fruits.count("Apple"))

new_fruits = ["Apple", "PineApple", "Green Apple"]
fruits.extend(new_fruits)
print(fruits)

print(fruits.count("Apple"))
print(fruits)
