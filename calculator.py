import math

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function square root
def square(x):
    return math.sqrt(x)

# This function caclulating factorial
def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact * i
    return fact

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Factorial")
print("6.Square Root")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # Check if choice is one of the six options
    if choice in ('1', '2', '3', '4', '5','6'):
        
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "+", num2, "=", add(num1, num2))
            
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            num1 = int(input("Enter first number: "))
            print("Factorial ", num1, "is ", factorial(num1))
        elif choice == '6':
            num1 = int(input("Enter first number: "))
            print("Square root of  ", num1, "is ", square(num1))
        break
    else:
        print("Invalid Input")