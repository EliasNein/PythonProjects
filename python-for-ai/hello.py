# %%
# IF STATEMENTS
# temperature = 24
# if temperature >= 30:
# 	print("It's very hot!")
# elif temperature >= 25 and temperature <= 29:
# 	print(f"it's hot")
# else:
# 	print("It's nice weather!")
# %%
#LOOPS
# for i in range(1, 10):
#     print(i)
# # %%
# for i in range(0, 10, 2):
#     print(i)
# %%
# LISTS

# fruits = ["apple", "banana", "orange"]

# # Get items
# print(fruits[0])    # "apple" (first item)
# print(fruits[1])    # "banana"
# print(fruits[-1])   # "orange" (last item)
# print(fruits[-2])   # "banana" (second to last)

# # Slicing
# print(fruits[0:2])  # ["apple", "banana"]
# print(fruits[1:])   # ["banana", "orange"]

# # Change an item
# fruits[0] = "mango"
# print(fruits)  # ["mango", "banana", "orange"]

# # Add items
# fruits.append("grape")      # Add to end
# fruits.insert(1, "kiwi")    # Insert at position

# # Remove items
# fruits.remove("banana")     # Remove by value
# last = fruits.pop()        # Remove and return last
# del fruits[0]              # Remove by index

# numbers = [3, 1, 4, 1, 5, 9]

# # Information
# print(len(numbers))         # 6 (length)
# print(numbers.count(1))     # 2 (count occurrences)
# print(numbers.index(4))     # 2 (find position)

# # Sorting
# numbers.sort()              # Sort in place
# print(numbers)              # [1, 1, 3, 4, 5, 9]

# numbers.reverse()           # Reverse order
# print(numbers)              # [9, 5, 4, 3, 1, 1]

# # Copy
# new_list = numbers.copy()   # Create a copy

# fruits = ["apple", "banana", "orange"]

# # Check if item exists
# if "apple" in fruits:
#     print("Found apple!")

# # Check if list is empty
# if fruits:
#     print("List has items")
# else:
#     print("List is empty")
# %%
#DICTIONARIES

# # Empty dictionary
# my_dict = {}

# # Dictionary with data
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# # Different ways to create
# scores = dict(math=95, english=87, science=92)

# # Get values by key
# print(person["name"])       # "Alice"
# print(person["age"])        # 30

# # Safer with get()
# print(person.get("job"))    # None (no error)
# print(person.get("job", "Unknown"))  # "Unknown" (default)

# person = {"name": "Alice", "age": 30, "city": "New York"}

# # Get all keys, values, or items
# print(person.keys())    # dict_keys(['name', 'age', 'city'])
# print(person.values())  # dict_values(['Alice', 30, 'New York'])
# print(person.items())   # dict_items([('name', 'Alice'), ...])

# # Check if key exists
# if "name" in person:
#     print("Name found!")

# # Update multiple values
# person.update({"age": 31, "job": "Engineer"})

# Dictionary of dictionaries
# students = {
#     "alice": {"age": 20, "grade": "A"},
#     "bob": {"age": 21, "grade": "B"},
#     "charlie": {"age": 19, "grade": "A"}
# }

# # Access nested data
# print(students["alice"]["grade"])  # "A"
# %%
#TUPLES

# Empty tuple
# empty = ()

# # Tuple with items
# point = (3, 5)
# colors = ("red", "green", "blue")

# # Single item tuple needs comma!
# single = (42,)  # Note the comma
# not_tuple = (42)  # This is just 42 in parentheses

# # Without parentheses (implicit)
# coordinates = 10, 20

# # Get items
# print(point[0])      # 3
# print(colors[-1])    # "blue"

# # Slicing works too
# print(colors[0:2])   # ("red", "green")

# # Unpack values
# x, y = point  # x = 3, y = 5

# # Multiple assignment
# a, b, c = 1, 2, 3  # Same as (1, 2, 3)

# # Swap variables elegantly
# x, y = y, x  # Swaps values
# %%
# SETS

# Empty set (careful!)
# empty_set = set()  # NOT {} - that's a dict!

# # Set with values - both ways work
# numbers = {1, 2, 3, 4, 5}
# fruits = set(["apple", "banana", "orange"])

# # From a list (removes duplicates)
# scores = [85, 90, 85, 92, 90]
# unique_scores = set(scores)  # {85, 90, 92}

# colors = {"red", "blue"}

# # Add items
# colors.add("green")
# print(colors)  # {'red', 'blue', 'green'}

# # Remove items
# colors.remove("blue")    # Error if not found
# colors.discard("yellow") # No error if not found

# # Check membership
# if "red" in colors:
#     print("Red is available")
    
# names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
# unique_names = list(set(names))
# print(unique_names)  # ['Alice', 'Bob', 'Charlie']

# allowed_users = {"alice", "bob", "charlie"}

# if "alice" in allowed_users:  # Very fast!
#     print("Access granted")