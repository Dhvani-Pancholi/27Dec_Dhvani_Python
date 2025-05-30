##### Understanding the concepts of classes, objects, attributes, and methods in Python.

1.Classes:

• A class is a blueprint or template for creating objects.
• It defines the structure and behavior (attributes and methods) that the objects created from the class will have.
• Use the class keyword to define a class.

2.Objects:

• An object is an instance of a class.
• When a class is instantiated, it creates an object.
Objects have attributes (data) and methods (functions) associated with them.
```python
Ex.
class data:
    id=7
    name= "Raj"
    def print_data(self):
        print("id: ", self.id)
        print("name: ",self.name)
dt=data()
dt.print_data()
```

3.Attributes:
• Attributes are variables that belong to an object.
• They store data or properties related to the object.
• You define attributes inside the class and initialize them using the _init_ method.

4.Methods:
• Methods are functions defined inside a class.
• They describe the behavior of the objects.
• Methods often operate on the object's attributes and can perform actions.
```python
Ex.
class stud:
    def _init_(self, id,name):
        self.id = id
        self.name = name
    def print_data(self):
        print(f"ID:{self.id} \nName:{self.name}")
s = stud("21", "mansi")
s.print_data()
```