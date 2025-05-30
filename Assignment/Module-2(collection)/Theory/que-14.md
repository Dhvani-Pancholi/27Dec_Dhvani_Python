##### Accessing, adding, updating, and deleting dictionary elements

**Accessing Elements**
Use the key to retrieve a value.

```python
my_dict = {"name": "Dhvani", "age": 22, "city": "Rjk"}
print(my_dict["name"])
```

**Adding Elements**
Add a new key-value pair.

```python
my_dict["country"] = "India"
print(my_dict)
```

**Updating Elements**
Modify the value of an existing key.

```python
my_dict["age"] = 23
print(my_dict) 
```

**Deleting Elements**
1.Remove a specific key-value pair using del:

```python
del my_dict["city"]
print(my_dict)  
```

2.Using pop() to remove and return a value:

```python
age = my_dict.pop("age")
print(my_dict)
```