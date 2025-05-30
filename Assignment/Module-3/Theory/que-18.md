##### using re.search() and re.match() functions in python’s re module for pattern matching 

re.search() :
```python
Ex: 
import re
mystr="This is Python!"
x=re.search('Python',mystr)
print(x)
if x:
    print("Match done!")
else:
    print("Error!")
```

re.match()
```python
Ex:
import re
mystr="This is Python!"
x=re.match('This',mystr)
print(x)
if x:
    print("Match done!")
else:
    print("Error!")
```