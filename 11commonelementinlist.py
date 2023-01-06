# Write a Python function that takes two lists and returns True if they have at least one common member. 
aList = [1,2,3,4,5]
bList = [6,7,8,9,10]
count = 0
for item in aList:
    for item2 in bList:
        if item == item2:
            count += 1
if count > 0:
    print("Common elements are present in both lists")
else:
    print("No common elements are present in both lists")
