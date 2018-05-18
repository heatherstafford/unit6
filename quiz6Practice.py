#Heather Stafford
#5/18/18
#quiz6Practice.py

file = open('engmix.txt')

#program 1
for line in file:
    word = line.lower()
    letterC = int(word.count('c'))
    letterP = int(word.count('p'))
    if letterC == 3 and letterP == 2:
        print(word)

#program 2
num = 0

for line in file:
    if len(line) > 0 and line[0] == 'r':
        num += 1

print(num)
    
#program 3
from random import randint

num = int(input('Enter a number: '))

L =[]

for line in file:
    if len(line) == num:
        L.append(line)

print(L[randint((0, len(L)+1)])
        
        