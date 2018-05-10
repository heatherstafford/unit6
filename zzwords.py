#Heather Stafford
#5/10/18
#zzwords.py

file = open('engmix.txt')

numWords = 0

for line in file:
    if 'zz' in line:
        print(line.strip())
    numWords += 1
    
print(numWords)
