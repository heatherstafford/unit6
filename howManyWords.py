#Heather Stafford
#5/10/18
#howManyWords.py

file = open('engmix.txt')

L = [0]*22

for line in file:
    if (len(line.strip())) > 0:
        L[len(line.strip())-1] += 1
    
for i in range(0,22):
    print(i,'letter words:', L[i - 1])