# Functions in Python
# Author: Ayesha Saleem


# -----------------------------------------------------
# 1. Simple Function (No Parameters)
# -----------------------------------------------------
def say_hello():
    print("Hello! Welcome to Python functions.")

say_hello()


# -----------------------------------------------------
# 2. Function with Parameters
# -----------------------------------------------------
def greet(name):
    print("Hello,", name)

greet("Ayesha")


# -----------------------------------------------------
# 3. Function with Return Value
# -----------------------------------------------------
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Addition Result:", result)


# -----------------------------------------------------
# 4. Function with Default Parameter
# -----------------------------------------------------
def introduce(name, course="Python"):
    print(f"My name is {name} and I am learning {course}.")

introduce("Ayesha")
introduce("Ayesha", "Machine Learning")


# -----------------------------------------------------
# 5. Function Using User Input
# -----------------------------------------------------
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("\nEnter a number: "))
print("The number is", check_even_odd(num))


# -----------------------------------------------------
# 6. Function with List
# -----------------------------------------------------
def calculate_total(marks):
    return sum(marks)

marks_list = [80, 75, 90, 85]
print("Total Marks:", calculate_total(marks_list))


# -----------------------------------------------------
# 7. Function Returning Multiple Values
# -----------------------------------------------------
def basic_calculator(a, b):
    return a + b, a - b, a * b

add, sub, mul = basic_calculator(10, 5)
print("\nCalculator Results:")
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)


# -----------------------------------------------------
# 8. *args (Variable Length Arguments)
# -----------------------------------------------------
def average(*numbers):
    return sum(numbers) / len(numbers)

print("\nAverage:", average(10, 20, 30, 40))


# -----------------------------------------------------
# 9. **kwargs (Keyword Arguments)
# -----------------------------------------------------
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print("\nStudent Information:")
student_info(name="Ayesha", course="Python", level="Beginner")

# -----------------------------------------------------
# 10. *args and **kwargs 
# -----------------------------------------------------
def log_messages(*args, **kwargs):
    print("\nLog Messages:")
    for message in args:
        print("-", message)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

log_messages(
    "System started",
    "Model loaded",
    status="Success",
    version="1.0"
)


# -----------------------------------------------------
# 11. Nested Function 
# -----------------------------------------------------
def outer_function():
    print("\nOuter function executed.")

    def inner_function():
        print("Inner function executed.")

    inner_function()

outer_function()


# -----------------------------------------------------
# 12. Recursive Function
# -----------------------------------------------------
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("\nFactorial of 5:", factorial(5))


# -----------------------------------------------------
# 13. Practical / ML-Style Utility Function
# -----------------------------------------------------
def min_max_scaler(data):
    minimum = min(data)
    maximum = max(data)
    return [(x - minimum) / (maximum - minimum) for x in data]

values = [50, 60, 70, 80, 90]
print("\nScaled Values:", min_max_scaler(values))



