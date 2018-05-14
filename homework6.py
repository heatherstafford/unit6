#Heather Stafford
#5/14/18
#homework6.py - how to struggle

file = open('engmix.txt')

word = input('Enter a word: ')

result = 'is not'

for line in file:
    if word == line.strip():
        result = 'is'
        
print('The word', result, 'in the dictionary')
