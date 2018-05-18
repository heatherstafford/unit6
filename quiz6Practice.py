#Heather Stafford
#5/18/18
#quiz6Practice.py

#program 1
file = open('engmix.txt')

"
for line in file:
    word = line.lower()
    letterC = int(word.count('c'))
    letterP = int(word.count('p'))
    if letterC == 3 and letterP == 2:
        print(word)
"    
