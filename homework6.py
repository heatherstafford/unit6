#Heather Stafford
#5/14/18
#homework6.py - how to struggle

"""
file = open('engmix.txt')

word = input('Enter a word: ')

result = 'is not'

for line in file:
    if word == line.strip():
        result = 'is'
        
print('The word', result, 'in the dictionary')
"""

file = open('engmix.txt')

L = []

for line in file:
    L.append(line.strip())

num = input('Enter a number: ')

if num<= 0 or num >= len(L)+1:
    print('Invalid number')
else:
    print(L[num - 1])