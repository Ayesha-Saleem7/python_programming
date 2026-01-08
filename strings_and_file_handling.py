# Strings & File Handling in Python
# Author: Ayesha Saleem


# -----------------------------------------------------
# 1. String Basics
# -----------------------------------------------------
print("\n--- String Basics ---")

name = "Ayesha Saleem"
course = "Python Programming"

print("Name:", name)
print("Course:", course)

# -----------------------------------------------------
# 2. String Indexing & Slicing
# -----------------------------------------------------
print("\n--- String Indexing & Slicing ---")

print("First character:", name[0])
print("Last character:", name[-1])
print("First 6 characters:", name[:6])
print("Last 6 characters:", name[-6:])

# -----------------------------------------------------
# 3. Common String Methods
# -----------------------------------------------------
print("\n--- String Methods ---")

text = " python learning journey "

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Stripped:", text.strip())
print("Replace:", text.replace("python", "AI"))
print("Length:", len(text))

# -----------------------------------------------------
# 4. String Formatting (Professional Way)
# -----------------------------------------------------
print("\n--- String Formatting ---")

age = 20
field = "AI & Machine Learning"

formatted = f"My name is {name}. I am {age} years old and learning {field}."
print(formatted)

# -----------------------------------------------------
# 5. Writing to a File
# -----------------------------------------------------
print("\n--- Writing to File ---")

file_name = "student_info.txt"

with open(file_name, "w") as file:
    file.write("Student Information\n")
    file.write(f"Name: {name}\n")
    file.write(f"Course: {course}\n")
    file.write(f"Interest: {field}\n")

print("Data written to file successfully.")

# -----------------------------------------------------
# 6. Appending to a File
# -----------------------------------------------------
print("\n--- Appending to File ---")

with open(file_name, "a") as file:
    file.write("\nStatus: Learning daily Python")

print("Data appended successfully.")

# -----------------------------------------------------
# 7. Reading from a File
# -----------------------------------------------------
print("\n--- Reading from File ---")

with open(file_name, "r") as file:
    content = file.read()
    print("\nFile Content:\n")
    print(content)

# -----------------------------------------------------
# 8. Reading File Line by Line
# -----------------------------------------------------
print("\n--- Reading Line by Line ---")

with open(file_name, "r") as file:
    for line in file:
        print(line.strip())

# -----------------------------------------------------
# 9. Real-world Example: Username Validation
# -----------------------------------------------------
print("\n--- Username Validation (String Logic) ---")

username = input("Enter username: ").strip()

if len(username) < 5:
    print("Username too short.")
elif " " in username:
    print("Username should not contain spaces.")
else:
    print("Username is valid.")


