#Heather Stafford
#5/11/18
#reverse.py

file = open('engmix.txt')

L = []

for line in file:
    L.append(line)
    
L.reverse()

print(L)
