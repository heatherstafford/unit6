#Heather Stafford
#5/10/18
#howManyWords.py

file = open('engmix.txt')

L = [0]*22

for line in file:
    L[len(line)-1] + 1

print(L)
