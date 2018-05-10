#Heather Stafford
#5/10/18
#howManyWords.py

file = open('engmix.txt')

L = [0]*22

for line in file:
    L[len(line.strip())-1] += 1
    
for item in L:
    print(item,'letter words:' len(L[item]))

