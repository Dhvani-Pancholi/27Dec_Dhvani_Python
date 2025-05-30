##### Different types of functions: with/without parameters, with/without return values.

**1.function without parameter and without return value**   

These functions neither accept input values nor return a result.
```python
def func():
    print("Hello")
func()
```
**2.function with parameter and without return value**
These functions accept input values but do not return a result.
```python
def func(name):
    print("Hello", name)
func("python")
```

**3.function without parameter and with return value**
These functions do not accept input values but return a result.
```python
def get_pi():
    return 3.14
pi = get_pi()
print(pi)
```

**4.function with parameter and with return value**
These functions accept input values and return a result.
```python
def add(a, b):
    return a + b
result = add(2, 4)
print(result)
```
