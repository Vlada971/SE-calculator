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
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))