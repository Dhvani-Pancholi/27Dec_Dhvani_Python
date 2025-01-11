#Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.

percentage = float(input("Enter Your percentage:"))
print("Percentage:", percentage)

if percentage > 80:
    print("Grade is A")
elif percentage > 70:
    print("Grade is B")
elif percentage > 60:
    print("Grade is C")
elif percentage > 50:
    print("Grade is D")
else:
    print("Grade is E")