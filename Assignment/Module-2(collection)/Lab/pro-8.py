# Write a Python program to insert elements into an empty list using a for loop and append().

list = []

n = int(input("Enter number of elements:"))

for i in range(n):
    a = input("Enter fruit name:")
    list.append(a)

print(list)