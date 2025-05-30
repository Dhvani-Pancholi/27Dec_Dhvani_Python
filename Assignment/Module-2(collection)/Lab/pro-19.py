#Write a Python program to merge two lists into one dictionary using a loop.
list1=["name","age","city"]
list2=["mina",20,"rajkot"]
data={}
for i in range(len(list1)):
    data[list1[i]]=list2[i]
print(data)
