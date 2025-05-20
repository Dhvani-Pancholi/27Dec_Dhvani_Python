#Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition.

List1 = ['apple', 'banana', 'mango','watermelon','cherry']

str = input("enter a string:")
bool = False
for  i in List1:
    if str == i:
        bool = True
if bool:
    print("String is found in list")
else:
    print("String is not found in list")