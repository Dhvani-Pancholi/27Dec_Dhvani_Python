##### Scope of variables in Python.

In Python, the scope of a variable is determined by where it is defined. If a variable is
defined inside a function, its scope is limited to that function. If a variable is defined
outside a function, its scope is global.

**Local Scope**
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

Example:
```python
def myfunc():
  x = 100
  print(x)

myfunc()
```

**Global Scope**

A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.

Example:
```python
x = 100
def myfunc():
  print(x)

myfunc()
print(x)
```