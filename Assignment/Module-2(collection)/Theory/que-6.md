#####  Iterating over a list using loops

**1.Using a for Loop**

Example:

```python
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)
```

**2.Using a While Loop**

Example:
```python
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1
```

**3.List Comprehension**

Example:
```python
a = [2,3,4,5]
res = [val ** 2 for val in a]
print(res)
```