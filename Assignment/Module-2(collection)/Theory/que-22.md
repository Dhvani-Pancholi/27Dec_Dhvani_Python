##### Introduction to Python modules and importing modules

A Python module is a file containing Python definitions and statements. A module can define functions, classes, and variables.

To use a module, you need to import it. Importing a module allows you to use its
functions, classes, and variables in your code.

**Importing Modules:**

**1.Importing an Entire Module**
You can import an entire module using the import statement:
```python
import math
print(math.sqrt(25))
```

**2.Importing Specific Functions or Variables**
You can import only specific functions or variables from a module:

```python
from math import sqrt, pi

print(sqrt(16))  
print(pi) 
```

**3.Importing with an Alias**
You can rename a module while importing to use a shorter name:

```python
import math as mt
print(mt.sqrt(25))
```

**4.Importing Everything from a Module**
You can import all functions and variables from a module using *:

```python
from math import *
print(floor(13.5))
```
