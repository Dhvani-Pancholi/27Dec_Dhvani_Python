#Write a Python program to read a string, an integer, and a float from the keyboard and display them.

f = open("stdata.txt","w")

id = int(input("Enter an ID:"))
name = input("Enter a Name:")
marks = float(input("Enter a marks:"))


f.write(f"ID:{id}\nName:{name}\nMarks:{marks}")

f = open("stdata.txt","r")
print(f.read())