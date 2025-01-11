#Practical Example 6: Write a Python program to check if a number is prime using if_else statement.

n = int(input("Enter a number:"))
prime = 0
for i in range (1,n+1):
    if n % i == 0:
        prime += 1
if prime == 2:
    print(n,"is Prime number")
else:
    print(n,"is not a prime number")