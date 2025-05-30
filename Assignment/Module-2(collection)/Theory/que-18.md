##### Counting occurrences of characters in a string using dictionaries

```python
data="hello python"
count={}
for i in data:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

```

