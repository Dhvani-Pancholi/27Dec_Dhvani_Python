#Write a Python program to create a class and access its properties using an object

class stuinfo:
    id = int
    name = str
    city = str

    def data(self):
        self.id = int(input("Enter the id:"))
        self.name = input("Enter the name:")
        self.city = input("Enter the city:")

    def print_data(self):
        print("Student ID:", self.id)
        print("Student Name:", self.name)
        print("Student City:", self.city)

st = stuinfo()
st.data()
st.print_data()
