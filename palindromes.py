#Heather Stafford
#5/16/18
#palindromes.py

file = open('engmix.txt')

new = ''
L = []

for line in file:
    L.append(line)
    new = L.reverse
    if line == new:
        print(line)