# Conditional Statements in Python
# Description:
# This program demonstrates decision-making using if, elif, and else, nested if & match case
# with multiple real-world inspired examples.

# --------------------------------------------------
# 1. Positive, Negative, or Zero
# --------------------------------------------------
number = int(input("\nEnter a number: "))

if number > 0:
    print("Result: Positive number")
elif number < 0:
    print("Result: Negative number")
else:
    print("Result: Zero")

# --------------------------------------------------
# 2. Even or Odd Check
# --------------------------------------------------
print("\nEven or Odd Check:")

if number % 2 == 0:
    print("Result: Even number")
else:
    print("Result: Odd number")

# --------------------------------------------------
# 3. Age-Based Category
# --------------------------------------------------
print("\nAge Category Check:")
age = int(input("Enter your age: "))

if age < 13:
    print("Category: Child")
elif age < 20:
    print("Category: Teenager")
elif age < 60:
    print("Category: Adult")
else:
    print("Category: Senior Citizen")

# --------------------------------------------------
# 4. Student Grade System
# --------------------------------------------------
print("\nStudent Grade Evaluation:")
marks = float(input("Enter marks (0 - 100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)

# --------------------------------------------------
# 5. Simple Login System
# --------------------------------------------------
print("\nLogin System:")

saved_username = "admin"
saved_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == saved_username and password == saved_password:
    print("Login successful!")
else:
    print("Invalid username or password.")

# --------------------------------------------------
# 6. Temperature-Based Recommendation
# --------------------------------------------------
print("\nWeather Recommendation System:")
temperature = float(input("Enter current temperature (°C): "))

if temperature < 15:
    print("Recommendation: Wear warm clothes.")
elif temperature <= 30:
    print("Recommendation: Weather is pleasant.")
else:
    print("Recommendation: Stay hydrated and avoid heat.")

# --------------------------------------------------
# 7. ATM Withdrawal Check
# --------------------------------------------------
print("\nATM Withdrawal System:")
balance = 50000
withdraw_amount = int(input("Enter withdrawal amount: "))

if withdraw_amount <= 0:
    print("Invalid withdrawal amount.")
elif withdraw_amount > balance:
    print("Insufficient balance.")
else:
    balance -= withdraw_amount
    print("Withdrawal successful.")
    print("Remaining balance:", balance)

# --------------------------------------------------
# 8. Simple AI-style Decision Example
# --------------------------------------------------
print("\nAI-style Health Recommendation:")
steps = int(input("Enter number of steps walked today: "))

if steps < 3000:
    print("Low activity level. Try to move more.")
elif steps < 8000:
    print("Good activity level. Keep it up!")
else:
    print("Excellent activity level. Great job!")

    # --------------------------------------------------
# 9. Nested if Example
# --------------------------------------------------
print("\nNested if Example: Scholarship Eligibility Check")

marks = float(input("Enter your marks (0 - 100): "))
attendance = int(input("Enter attendance percentage: "))

if marks >= 80:
    if attendance >= 75:
        print(" Eligible for Scholarship")
    else:
        print(" Not eligible (Attendance below 75%)")
else:
    print("Not eligible (Marks below 80%)")

 # --------------------------------------------------
# 10. Switch-Case Style Example (match-case)
# Python 3.10+
# --------------------------------------------------
print("\nMenu Selection System (Switch-Case Style):")

print("1. Check Balance")
print("2. Deposit Money")
print("3. Exit")

choice = int(input("Enter your choice (1-3): "))

match choice:
    case 1:
        print("Your current balance is Rs. 50,000")
    case 2:
        amount = int(input("Enter amount to deposit: "))
        print("Rs.", amount, "deposited successfully.")
    case 3:
        print("Thank you for using our service.")
    case _:
        print("Invalid choice. Please select a valid option.")




