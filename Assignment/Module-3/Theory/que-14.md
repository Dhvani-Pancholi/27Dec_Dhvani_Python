##### Single, Multilevel, Multiple, Hierarchical, and Hybrid inheritance in Python.

**1.Single Inheritance**
In single inheritance, a child class inherits from a single parent class. 
```python
Ex.
class father:
    def get_data(self):
    print("This Is Parent Class")
class daughter(father):
    def get_child_data(self):
    print("This Is Child Class")
d=daughter()
d.get_data()
d.get_child_data()
```

**2.Multilevel Inheritance**
In multilevel inheritance, a class inherits from a parent class, and another class inherits from this child class, forming a chain.
```python
Ex.
class grandparent:
    def getdata(self):
    print("This Is GrandParent Class")
class parent(grandparent):
    def get_data(self):
    print("This Is Parent Class")
class child(parent):
    def get_child_data(self):
    print("This Is Child Class")
c=child()
c.getdata()
c.get_data()
c.get_child_data()
```

**3.Multiple Inheritance**
In multiple inheritance, a child class inherits from two or more parent classes. 
This allows the child class to access properties and methods of all its parents.
```python
Ex.
class Daughters:
    def getdata1(self):
    print("Hello From Daughters")
class Son:
    def getdata2(self):
    print("Hello From Son")
class Parents(Daughters,Son):
    def getdata(self):
    print("Hello From Parents")
p=Parents()
p.getdata()
p.getdata1()
p.getdata2()
```

**4.Hierarchical Inheritance**
In hierarchical inheritance, multiple child classes inherit from a single parent class. This is useful when several classes share the same base functionality.
```python
Ex.
class Parents:
    def getdata(self):
    print("This is parents class!")
class Daughters(Parents):
    def getdata1(self):
    print("This is daughters class!!!")
class Son(Parents):
    def getdata2(self):
    print("This is son's class!!!")
obj1=Son()
obj1.getdata()
obj1.getdata2()
obj2=Daughters()
obj2.getdata()
obj2.getdata1()
```

**5.Hybrid Inheritance**
Hybrid inheritance combines two or more types of inheritance to form a more complex hierarchy.
```python
Ex.
class Parents:
    def getdata(self):
    print("Hello from parents")
class Child1(Parents):
    def getdata1(self):
    print("Hello from Child1")
class Child2(Parents):
    def getdata2(self):
    print("Hello from Child2")
class GrandChild(Child1,Child2):
    def getdata3(self):
    print("Hello from Grandchild")
g=GrandChild()
g.getdata()
g.getdata1()
g.getdata2()
g.getdata3()
```