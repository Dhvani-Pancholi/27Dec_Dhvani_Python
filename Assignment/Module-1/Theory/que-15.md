##### How loops work in Python.

In Python, loops are used to execute a block of code repeatedly as long as a certain condition is met. Python supports two main types of loops: for loops and while loops.

1.for Loop
- The for loop is used to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code for each element in the sequence.

Syntax:
```python
for variable in sequence:
    # code to execute
```
Example of for loop:
```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

Using range() in a for loop
- The range() function generates a sequence of numbers.

```python

for i in range(5):
    print(i)
```

2.while Loop
- The while loop is used to execute a block of code as long as a given condition is True. If the condition becomes False, the loop stops.

Syntax:
```python
while condition:
    # Code to execute
```
Example of a while loop :
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```    