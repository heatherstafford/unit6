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
    
"""
    
#Program #3
number3 = input('Enter a number: ')
letter3 = input('Enter a letter: ')

for line in file:
    if len(line.strip()) == number3 and line[0] == letter3:
        print(line)
