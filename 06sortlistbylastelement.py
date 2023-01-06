'''6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]'''
aList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
bList = []
fList = []
for i in range(0, len(aList)):
    bList.append(aList[i][1])
bsList = sorted(bList)
print(bsList)

for i in range(0, len(bsList)):
    for j in range(0, len(bsList)):
        if bsList[i] == aList[j][1]:
            fList.append(aList[j])
print(fList)
