# Write a Python program to count how many times each character appears in a string.

data="hello python"
count={}
for i in data:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
