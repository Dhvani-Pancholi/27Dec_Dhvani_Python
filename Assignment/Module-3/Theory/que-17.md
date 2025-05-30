##### Method overriding: redefining a parent class method in the child class.
 
Method overriding occurs when a child class provides a specific implementation for a method that is already defined in its parent class.

The overriding method in the child class must have the same name, parameters, and return type as the method in the parent class.
```python
Ex.
class Parent:
    def getdata(self):
    print("Hello from parent's class")
class Child(Parent):
    def getdata(self):
    print("Hello from child's class")
c=Child()
c.getdata()
p=Parent()
p.getdata()
```