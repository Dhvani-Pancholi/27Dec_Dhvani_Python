##### Understanding multiple exceptions and custom exceptions.

Python allows you to handle multiple exceptions using multiple except 
blocks or by combining them into a single block.

Sometimes, different types of errors can occur in a program, and you may want 
to handle them separately.

- Multiple exception:
```python
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Division by zero is not allowed!")
except Exception as e:
    print("An unexpected error occurred:", e)
    print("Program continues...")
```

- Custom exception: 
```python
try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print("Sum:",a+b)
except:
    print("Error!")
```