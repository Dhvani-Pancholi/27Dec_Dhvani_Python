##### opening files in different modes (‘r’, ‘w’, ‘a’, 'r+', 'w+')

```python
fl= open("info.txt", 'x')
fl = open("info.txt", 'w')
fl.write("Hello python")
fl = open("info.txt" , 'r')
print(fl.read())
fl=open("info.txt",'a')
fl.write("\nThis is programming language")
fl=open("info.txt", 'r+')
print(fl.write("\nThis is high level programming language"))
print(fl.read())
fl=open("info.txt", 'w+')
print(fl.write("\nThis is high level programming language"))
print(fl.read())
```