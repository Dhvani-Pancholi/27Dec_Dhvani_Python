#####  Understanding how to access and manipulate strings

#####  Accessing Strings :
To access a character in a string, you can use the index of the character. 

In Python,the index starts at 0, so the first character in a string is at index 0,the second character is at index 1, and so on.

```python
string = "Dhvani"
print(string[1])
```

##### Manipulate strings :
You can manipulate strings by using various methods such as lower, upper, and replacing.

text = "Hello Python!"

###### Convert to lowercase 
print(text.lower())  

###### Convert to uppercase
print(text.upper())

###### Replace a substring
print(text.replace("Python","World"))