#####  Iterating over a dictionary using loops

**1.Iterating over keys**
You can iterate through the dictionary keys using a simple for loop:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)
```

**2.Iterating over values**
To iterate over the values of the dictionary:

```python
for value in my_dict.values():
    print(value)
```

**3.Iterating over key-value pairs**
You can iterate over both keys and values using the items() method:

```python
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
``` 