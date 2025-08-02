def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x/y


print("Select Operation")
print("+ Add")
print("- Subtract")
print("* Multiply")
print("/ Divide")


choice = input("Enter Your Choice: ")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if choice == "+":

    print(num1, "+", num2, "=", add(num1,num2))

if choice == "-":
    print(num1, "-", num2, "=", subtract(num1,num2))

if choice == "*":
    print(num1, "*", num2, "=", multiply(num1,num2))

if choice == "/":
    print(num1, "/", num2, "=", divide(num1,num2))

next_choice = (input("Do you wanna continue with the calculation (yes/no): ").lower())
if next_choice == "no":
    print("Thank you for using this calculator.")
    exit()
