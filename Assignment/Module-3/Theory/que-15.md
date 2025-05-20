##### Using the super() function to access properties of the parent class.
```python
class stud_info:
    def info(self,id,name):
    print("id: ", id)
    print("name: ", name)
class data(stud_info):
    def info(self, id, name):
        return super().info(id, name)
dt=data ()
dt.info(7, "piya")
```