# Create a mini-project where students combine conditional statements, loops, and functions
# to create a basic Python application, such as a simple calculator

def add(a,b):
    print(f"Addition of given number is: {a+b}")

def sub(a,b):
    print(f"Subtraction of given number is: {a-b}")

def mul(a,b):
    print(f"Multiplication of given number is: {a*b}")

def div(a,b):
    print(f"Division of given number is: {a/b}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while True:
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. Exit")

    choice = input("Enter your choice(1,2,3,4,5): ")
    
    if choice == '1':
        add(num1,num2)
    elif choice == '2':
        sub(num1,num2)
    elif choice == '3':
        mul(num1,num2)
    elif choice == '4':
        div(num1,num2)
    elif choice == '5':
        print("Existing the program")
        break
    else:
        print("Invalid choice")
