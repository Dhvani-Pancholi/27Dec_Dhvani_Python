##### Writing to a file using write() and writelines()

**write**
```python
f=open("file.txt","w")
print(f.write("hello students\nWelcome to the python programming")) 
```

**writelines()**
```python
f = open("file.txt", "a")
f.writelines(["hello sir!", "How are you?"])
f.close()
```