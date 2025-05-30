#Write a Python program to open a file in write mode, write some text, and then close it

f = open("info.txt","w")

id = int(input("Enter an ID:"))
name = input("Enter a Name:")

f.write(f"ID:{id}\nName:{name}\n")
f.close()