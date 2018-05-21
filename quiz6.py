#Heather Stafford
#5/21/18
#quiz6.py

file = open('engmix.txt')

"""
#Program #1
letter1 = input('Enter a letter: ')

for line in file:
    if line.count(letter1) >= 4:
        print(line.strip())
    
#Program #3
number3 = int(input('Enter a number: '))
letter3 = input('Enter a letter: ')

for line in file:
    word = line.strip()
    if len(word)>0:
        if word[0] == letter3 and len(word) == number3:
            print(word)
"""

#Program #5
vowelnumber = 0
word = ''

for line in file:
    avowel = line.count('a')
    evowel = line.count('e')
    ivowel = line.count('i')
    ovowel = line.count('o')
    uvowel = line.count('u')
    newvowels = avowel + evowel + ivowel + ovowel + uvowel
    if newvowels > vowelnumbers:
        vowelnumber += newvowels
        word = line
print(word)
    