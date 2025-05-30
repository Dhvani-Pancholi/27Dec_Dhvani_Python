##### Understanding the role of break, continue, and pass in Python loops

**The break Statement:**

With the break statement we can stop the loop before it has looped through all the items:

Example : Exit the loop when x is "banana":

```python
for i in range(1,11):
  print(i)
  if i == 5:
    break
```
**The continue Statement:**

With the continue statement we can stop the current iteration of the loop, and continue with the next iteration

Example : 
```python
for i in range(1,11):
  if i==7:
    continue
  print(i)
```
**The pass Statement:**

The pass statement in Python is a null operation — when it is executed, nothing happens. 

It is a placeholder when a statement is required syntactically but no execution of code is necessary.

```python
for x in range(1,11):
  pass
```