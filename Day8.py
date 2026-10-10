#Day 8 practice

def add(a,b):
        return a+b
print(add(5,6))

print(add(746,34))


def greet(name):
    print(f" Welcome to the Social Eagle Community: {name}")


greet("Dhruva")



#Assignment 


# Calculator using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b


while True:

    num1 = float(input("Enter First Number : "))
    num2 = float(input("Enter Second Number : "))

    print("\n===== Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":
        print("Result =", add(num1, num2))

    elif choice == "2":
        print("Result =", subtract(num1, num2))

    elif choice == "3":
        print("Result =", multiply(num1, num2))

    elif choice == "4":
        print("Result =", divide(num1, num2))

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid Choice")