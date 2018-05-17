#Heather Stafford
#5/16/18
#palindromes.py

file = open('engmix.txt')

for line in file:
    new = ''
    word = line.strip()
    for ch in word:
        new = ch + new
    if new == word:
        print(word)
    