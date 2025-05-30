'''Write Python programs to demonstrate different types of inheritance 
(single, multiple, multilevel, etc.)'''

# SINGLE INHERITANCE
class Student:
    st_id=int
    st_name=str
    def get_data(self):
        self.id = input("Enter an id: ")
        self.name=input("Enter a name: ")
        print("This is Main class")

class Child(Student):
    def print_data(self):
        print("Id is: ",self.id)
        print("Name is: ",self.name)
        print("This is Sub class")
    
c=Child()
c.get_data()
c.print_data()

# MULTIPLE INHERITANCE

class GrandParent:
    def getdata(self):
        print("This Is Grandparent Class")

class Parent:
    def getdata1(self):
        print("This Is Parent Class")

class Child(GrandParent,Parent):
    def getdata2(self):
        print("This Is Child Class")

c=Child()
c.getdata()
c.getdata1()
c.getdata2()

# MULTILEVEL INHERITANCE

class raj:
    a_id=0
    a_nm=""

    def getdata(self):
        self.a_id=input("Enter raj's Id: ")
        self.a_nm=input("Enter raj's father Name: ")

class mina(raj):
    jid=0
    jnm=""

    def getdata2(self):
        self.jid=input("Enter mina's Id: ")
        self.jnm=input("Enter mina's father Name: ")

class priya(mina):
    an_id=0
    an_nm=""

    def getdata3(self):
        self.an_id=input("Enter priya's Id: ")
        self.an_nm=input("Enter priya's father Name: ")

class chen(priya):
    def printdata(self):
        print("-----------raj's Info--------------")
        print("raj's ID: ",self.a_id)
        print("raj's Name: ",self.a_nm)
        print("-------------mina's Info-------------")
        print("mina's ID: ",self.jid)
        print("mina's Name: ",self.jnm)
        print("-------------priya's Info-------------")
        print("priya's ID:",self.an_id)
        print("priya's Name: ",self.an_nm)

k=chen()
k.getdata()
k.getdata2()
k.getdata3()
k.printdata()