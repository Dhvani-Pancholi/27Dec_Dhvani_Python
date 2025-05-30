##### Method overloading: defining multiple methods with the same name but different parameters.

Python does not support method overloading. 

Ex. It’s return error
```python
class studinfo:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)
 
    def getdata(self,sal):
        print("Salary:",sal)
st=studinfo()
st.getdata(101,'aniket')
st.getdata(487.44)
```