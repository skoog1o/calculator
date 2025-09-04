#calculator
def sum(a,b): #function to add two numbers
    return (a+b)

# accept an int from user
a = int(input("Enter 1st number: "))

# accept an int from user
b = int(input('Enter 2nd number: '))

# print results
print(f'Sum of {a} and {b} is {sum(a,b)}')

# define math operations
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y != 0:
        return x/y
    else:
            return "Error! Not possible to divide by zero."

# User Interface
print("Select operation:")
print('1. ADD')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

# accept input from user
choice = input('Enter choice(1/2/3/4): ')
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# Calculating the user's input
if choice == "1":
    print(f'{num1} + {num2} = {add(num1,num2)}')
elif choice == "2":
    print(f'{num1} - {num2} = {subtract(num1,num2)}')
elif choice == "3":
    print(f'{num1} * {num2} = {multiply(num1,num2)}')
elif choice == "4":
    print(f'{num1} / {num2} = {divide(num1,num2)}')
else:
    ('Invalid Input')
