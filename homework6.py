

file = open('engmix.txt')

word = input('Enter a word: ')

for line in file:
    if word == line.strip():
        result = 'is'
        
print('The word', result, 'in the dictionary')
