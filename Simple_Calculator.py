# Function for addition
def add(a, b):
    return a + b


# Function for subtraction
def sub(a, b):
    return a - b


# Function for multiplication
def mul(a, b):
    return a * b


# Function for division
def div(a, b):
    if b == 0:
        return "undefined"
    return a / b


# Function for percentage
def mod(a, b):
    if b == 0:
        return "undefined"
    return a % b


# Function for exponent
def pow(a, b):
    return a ** b


# get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operand = input("Enter operand: (+,-,*,/,%,**)")

# Calculations
if operand == "+":
    result = (add(num1, num2))
elif operand == "-":
    result = (sub(num1, num2))
elif operand == "*":
    result = (mul(num1, num2))
elif operand == "/":
    result = (div(num1, num2))
elif operand == "%":
    result = (mod(num1, num2))
elif operand == "**":
    result = (pow(num1, num2))
else:
    result = "Invalid operand"

# space
print()

# result
print("Result =", result)