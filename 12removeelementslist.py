''' Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']'''
aList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
nList = [0,4,5]
sList = []
for i in range(0, len(aList)):
    if i not in nList:
        sList.append(aList[i]) 
print(sList)
