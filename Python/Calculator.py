#Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Welcome to the state of the art calculator!\n")
print("What math are you doing")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

operator = input("\nPick a number from the list above: ")

num_1 = float(input("\nPlease input the first number: "))
num_2 = float(input("Please input the second number: " ))

if operator == '1':
    print(num_1, "+", num_2, "=", add(num_1,num_2))

elif operator == '2':
    print(num_1, "-", num_2, "=", subtract(num_1,num_2))

elif operator == '3':
    print(num_1, "*", num_2, "=", multiply(num_1,num_2))

elif operator == '4':
    print(num_1, "/", num_2, "=", divide(num_1,num_2))

else:
    print("Somethin went wrong - make sure to use only numbers and symbols!")
