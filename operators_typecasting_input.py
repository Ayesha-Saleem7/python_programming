# Operators, Type Casting & User Input
# Author: Ayesha Saleem

# -----------------------------
# 1. Arithmetic Operators
# -----------------------------
a = 10
b = 3

print("Arithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print()

# -----------------------------
# 2. Comparison Operators
# -----------------------------
print("Comparison Operators:")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)
print()

# -----------------------------
# 3. Logical Operators
# -----------------------------
x = True
y = False

print("Logical Operators:")
print("x and y :", x and y)
print("x or y  :", x or y)
print("not x   :", not x)
print()

# -----------------------------
# 4. Type Casting
# -----------------------------
print("Type Casting:")
num_str = "25"
num_int = int(num_str)
num_float = float(num_int)

print("String to Integer:", num_int)
print("Integer to Float:", num_float)
print()

# -----------------------------
# 5. User Input
# -----------------------------
print("User Input Example:")
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nUser Details:")
print("Name:", name)
print("Age:", age)

# -----------------------------
# 6. Simple Calculation using Input
# -----------------------------
birth_year = 2026 - age
print("Estimated Birth Year:", birth_year)

