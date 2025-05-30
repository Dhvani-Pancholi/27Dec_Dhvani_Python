##### Merging two lists into a dictionary using loops or zip()

**1.Using a loop**
Example:

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]

merged_dict = {}
for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

print(merged_dict)
```

**2.Using zip()**
You can use the zip() function, which pairs elements from two lists into tuples and allows you to convert them into a dictionary directly:

```python

keys = ['a', 'b', 'c']
values = [1, 2, 3]

merged_dict = dict(zip(keys, values))

print(merged_dict)
```