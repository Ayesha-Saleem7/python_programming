# Python Data Structures
# Author: Ayesha Saleem

# -----------------------------------------------------
# 1. LISTS (Mutable, Ordered)
# -----------------------------------------------------
print("\n--- Lists ---")

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

# Indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Slicing
print("First three elements:", numbers[0:3])
print("From index 2 to end:", numbers[2:])

# List modification
numbers.append(60)
numbers.remove(20)
print("Updated list:", numbers)

# List comprehension (Professional practice)
squares = [n ** 2 for n in numbers]
print("Squared values:", squares)


# -----------------------------------------------------
# 2. TUPLES (Immutable, Ordered)
# -----------------------------------------------------
print("\n--- Tuples ---")

coordinates = (10.5, 20.3, 30.8)
print("Tuple:", coordinates)

# Indexing
print("First value:", coordinates[0])

# Slicing
print("First two values:", coordinates[:2])

# Tuple unpacking
x, y, z = coordinates
print("Unpacked values:", x, y, z)


# -----------------------------------------------------
# 3. SETS (Unique, Unordered)
# -----------------------------------------------------
print("\n--- Sets ---")

skills = {"Python", "ML", "AI"}
skills.add("Data Science")
skills.add("Python")  # Duplicate ignored

print("Skills set:", skills)

# Set operations
backend = {"Python", "Django", "SQL"}
data = {"Python", "Pandas", "NumPy"}

print("Common skills:", backend & data)
print("All skills:", backend | data)

# NOTE: Sets do NOT support indexing or slicing
print("Sets do not support indexing or slicing ")


# -----------------------------------------------------
# 4. DICTIONARIES (Key-Value Pairs)
# -----------------------------------------------------
print("\n--- Dictionaries ---")

student = {
    "name": "Ayesha",
    "age": 20,
    "course": "Python",
    "level": "Beginner"
}

# Accessing values using keys
print("Name:", student["name"])
print("Course:", student.get("course"))

# Updating dictionary
student["level"] = "Intermediate"

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)

# Dictionary keys & values
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))


# -----------------------------------------------------
# 5. Nested Data Structures
# -----------------------------------------------------
print("\n--- Nested Data Structures ---")

students = [
    {"name": "Ayesha", "marks": [80, 85, 90]},
    {"name": "Ali", "marks": [70, 75, 78]},
]

for s in students:
    avg = sum(s["marks"]) / len(s["marks"])
    print(f"{s['name']} Average Marks:", avg)


# -----------------------------------------------------
# 6. Dictionary & List Comprehension
# -----------------------------------------------------
print("\n--- Comprehensions ---")

square_dict = {n: n ** 2 for n in range(1, 6)}
print("Squares dictionary:", square_dict)

even_numbers = [n for n in range(1, 21) if n % 2 == 0]
print("Even numbers:", even_numbers)


# -----------------------------------------------------
# 7. ML-style Data Preparation Example
# -----------------------------------------------------
print("\n--- ML-style Data Example ---")

dataset = [45, 60, 75, 90, 100]

# Normalization
normalized = [(x - min(dataset)) / (max(dataset) - min(dataset)) for x in dataset]
print("Normalized data:", normalized)







