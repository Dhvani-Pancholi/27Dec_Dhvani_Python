#Write a Python program to write multiple strings into a file.

fl=open("test.txt","w")
fl.writelines("hello student \nthis is python. \npython is programming language.")
print(fl)