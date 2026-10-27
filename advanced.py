# Question 1: Multi-Step Arithmetic Operations
# Start with some base values
import math


a = 5
b = 10
c = 7
# TODO: Add 3 to a using +=
a += 3 
# TODO: Multiply b by 2 using *=
b *= 2
# TODO: Modulo c by 4 using %=
c %= 4

#TODO: Calculate the square root of (a^2 + b^2 + c^2)
result = math.sqrt(a**2 + b**2 + c**2)
print(f"Final result: {result:.2f}")

# Question 2: Complex Conditional Evaluation
# TODO: Input x, y, z
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
#TODO: Create conditions:
is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 <= z <= 50
#TODO: Create final_condition = is_even and is_positive and is_in_range
final_condition = is_even and is_positive and is_in_range
#TODO: Print final_condition
print("x is even:", is_even)
print("y is positive:", is_positive)
print("z is in range:", is_in_range)
print("Final condition:", final_condition)

#Grading with Adjustments
#TODO: Ask the user for their base score
base_score = int(input("Enter your base score: "))

base_score += 5  # Apply bonus points
base_score -= 10
  # Clamp the score between 0 and 100
final_score = max(0, min(base_score, 100))
#TODO: use if-elif-else to determine grade and print it
if final_score >= 90:
    grade = 'A'
elif final_score >= 80:
    grade = 'B'
elif final_score >= 70:
    grade = 'C'
elif final_score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Final score: {final_score}, Grade: {grade}")

#Question 4: Advanced Calculator
#TODO: Input num1, num2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
#TODO: Input operation 
operation = input("Enter operation (+, -, *, /, %, **): ")
#TODO: Match operation using if-elif
try:
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    elif operation == '**':
        result = num1 ** num2
    else:
        result = None
        print("Invalid operation")

    if result is not None:
        print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division or modulus by zero is not allowed.")
