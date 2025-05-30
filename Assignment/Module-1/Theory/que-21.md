##### Function arguments (positional, keyword, default).

**1.Positional Arguments**
These arguments are passed to a function based on their position. The order of the arguments matters.

Example:
```python
def data(fname, lname):
    print(f"Hello,{fname}{lname}")

data("Dhvani"," Pancholi")
```

**2.Keyword Arguments**
Keyword arguments are passed with a name (key) explicitly associated with their value. The order does not matter when using keyword arguments.

Example:
```python
def data(name, age):
    print(name,age)
data(age=22, name="Dhvani") 
```

**3.Default Arguments:**
You can assign default values to arguments in the function definition. If the argument is not provided when the function is called, the default value is used.

Example:
```python
def my_function(city = "Rajkot"):
  print("I am from " + city)

my_function("Surat")
my_function("Jamnagar")
my_function()
```
