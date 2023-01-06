# Write a Python program to find the list of words that are longer than n from a given list of words. 
sList = ["of", "and", "cat", "Daniel", "Steven", "Nutan", "Python", "Java"]
n = 3
for item in sList:
    if len(item) > n:
        print(item)
