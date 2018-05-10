#Heather Stafford
#5/10/18
#howManyWords.py

file = open('engmix.txt')

L = [0]*22

for line in file:
    L[len(line.strip())-1] += 1
    
for i in range(0,23):
    print(L[i],'letter words:' L[item]))