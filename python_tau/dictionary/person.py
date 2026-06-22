person1 = {"name": "Srinivas", "age": 36, "gender": "male"}

print(person1)

# Get Method to get individual value
name = person1.get("name")
print(f"Name is: {name}")

# Items method is to get dictionary list of items in key, value pair
print(person1.items())

# Keys method is to get dictionary list of Keys
print(person1.keys())

# popitem() - Removes last item from dictionary
person1.popitem()
print(person1)

# Set Defaults
person1.setdefault("gender", "male")
print(person1)

# Update method: Update dict1 with dict2
person1_newInfo = {"salary": 40000, "location": "Hyderabad"}
person1.update(person1_newInfo)
print(person1)

# Update existing items in dictionary with same key
person1_newdata = {"location": "Bangalore"}
person1.update(person1_newdata)
print(person1)


person1.update(name="Kadiyala")
print(person1)

person1.update(married=True)
print(person1)
