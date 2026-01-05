
#  Loops in Python

# ------------------------------------------------
# 1. for loop (basic)
# ------------------------------------------------
print("\n1. for loop example:")

for i in range(1, 6):
    print("Iteration:", i)

# ------------------------------------------------
# 2. while loop (basic)
# ------------------------------------------------
print("\n2. while loop example:")

count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# ------------------------------------------------
# 3. range() function
# ------------------------------------------------
print("\n3. range() examples:")

print("range(5):")
for i in range(5):
    print(i, end=" ")

print("\nrange(1, 10, 2):")
for i in range(1, 10, 2):
    print(i, end=" ")

print()

# ------------------------------------------------
# 4. break statement
# ------------------------------------------------
print("\n4. break statement:")

for num in range(1, 10):
    if num == 5:
        print("Loop stopped at", num)
        break
    print(num)

# ------------------------------------------------
# 5. continue statement
# ------------------------------------------------
print("\n5. continue statement:")

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# ------------------------------------------------
# 6. pass statement
# ------------------------------------------------
print("\n6. pass statement:")

for i in range(1, 4):
    if i == 2:
        pass   # placeholder
    print("Value:", i)

# ------------------------------------------------
# 7. Nested loops
# ------------------------------------------------
print("\n7. Nested loops (pattern):")

for row in range(1, 4):
    for col in range(1, 4):
        print("*", end=" ")
    print()

# ------------------------------------------------
# 8. Loop with else
# ------------------------------------------------
print("\n8. Loop with else:")

for i in range(1, 6):
    print(i)
else:
    print("Loop completed successfully")

# ------------------------------------------------
# 9. while loop with else
# ------------------------------------------------
print("\n9. while loop with else:")

n = 1
while n <= 3:
    print("n =", n)
    n += 1
else:
    print("While loop finished")


# ------------------------------------------------
# 10. Real-world example: Login system
# ------------------------------------------------
print("\n11. Login system example:")

correct_password = "python123"

while True:
    user_input = input("Enter password: ")
    
    if user_input == correct_password:
        print("Login successful!")
        break
    else:
        print("Wrong password, try again")

# ------------------------------------------------
# 11. Real-world example: Sum of numbers
# ------------------------------------------------
print("\n12. Sum of first N numbers:")

n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

# ------------------------------------------------
# 12. Mini ML-style thinking example
# ------------------------------------------------
print("\n13. ML-style training loop example:")

epochs = 5

for epoch in range(1, epochs + 1):
    print(f"Training model... Epoch {epoch}")


