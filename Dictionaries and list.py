 #Creating a list of numbers
numbers_list = [10, 20, 30, 40, 50]
print("List of Numbers:", numbers_list)

# Adding an element to the list
numbers_list.append(60)
print("\nAfter adding an element to the list:")
print(numbers_list)

# Removing an element from the list
numbers_list.remove(20)
print("\nAfter removing an element from the list:")
print(numbers_list)

# Creating a dictionary with key-value pairs
person_dict = {"name": "John", "age": 28, "city": "New York"}
print("\nDictionary with Key-Value Pairs:", person_dict)

# Changing a value in the dictionary
person_dict["age"] = 29
print("\nAfter changing a value in the dictionary:")
print(person_dict)

# Adding a new key-value pair to the dictionary
person_dict["country"] = "USA"
print("\nAfter adding a new key-value pair to the dictionary:")
print(person_dict)

# Removing a key-value pair from the dictionary
del person_dict["city"]
print("\nAfter removing a key-value pair from the dictionary:")
print(person_dict)