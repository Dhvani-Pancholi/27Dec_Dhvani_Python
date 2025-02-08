##### Slicing a list: accessing a range of elements.

Slicing a list in Python allows you to access a specific range of elements from a list. Slicing is done using the syntax:

```python
list[start:stop:step]
```
where:
- start: The index to begin the slice (inclusive).
- stop: The index to end the slice (exclusive).
- step: The interval between elements (optional).

```python
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[1:])
print(list[:7])
print(list[3:8:2])
print(list[-3:])
```

