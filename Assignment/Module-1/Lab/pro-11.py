#Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if.

age = int(input("Enter Your Age:"))
weight=int(input("Enter Your weight:"))

if age > 18:
    if weight >= 55:
        print("Person is Eligible for donate blood")
    else:
        print("Person is Not Eligible for donate blood")
else:
    print("Person is Not Eligible for donate blood")