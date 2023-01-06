#7. Write a Python program to remove duplicates from a list. 
aList = [1,2,3,4,4,5,6,6,7,8,9]
sList = []
for item in aList:
    if item not in sList:
        sList.append(item)
print(sList)
