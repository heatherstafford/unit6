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
for line in file:
    word = line.strip()
    num = 0
    if len(word) > 0:
        if word[0] = 'r':
        num += 1

print(num)
    