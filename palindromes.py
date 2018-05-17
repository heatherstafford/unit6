#Heather Stafford
#5/16/18
#palindromes.py

file = open('engmix.txt')

new = ''

for line in file:
    word = line.strip()
    for ch in word:
        new = ch + new
    if new == word:
        print(line.strip)
    