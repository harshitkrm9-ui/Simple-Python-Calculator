print("Welcome to the simplest calculator")

Num1 = float(input("Enter first number: "))
Num2 = float(input("Enter second number: "))
Operation = input("Enter the operation you want to perform (A/M/S/D): ").upper()
while Num2 == 0 and Operation == "D":
    print("Sorry, but the second number cannot be 0 for division.")
    Num2 = float(input("Enter second number again: "))

def Addition():
    Sum = Num1 + Num2
    return Sum

def Multiplication():
    Product = Num1 * Num2
    return Product

def Division():
    Quotient = Num1 / Num2
    return Quotient

def Subtraction():
    Difference = Num1 - Num2
    return Difference

if Operation == "A":
    print("The sum of those two numbers is ", Addition())
elif Operation == "M":
    print("The product of those two numbers is ", Multiplication())
elif Operation == "D":
    print("The quotient of those two numbers is ", Division())
elif Operation == "S":
    print("The difference of those two numbers is ", Subtraction())