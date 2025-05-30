##### Introduction to exceptions and how to handle them using try, except, and finally

Use try, except, and finally blocks:
- 1.try: Use try to test for errors.
- 2.except: Use except to handle specific errors.
- 3.finally: Code that always runs, even if there's an error.

```python
try:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    print("Sum: ",a+b)
except Exception as e:
    print(e)
finally:
    print("This is finally block")
```