#Write a Python program to read a name and age from the user and print a formatted output.

f = open("data.txt","w")
name = input("Enter your name: ")
age = input("Enter your age: ")
f.write(f"name:{name}\nage:{age}")

f = open("data.txt","r")
data = f.read()