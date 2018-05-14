

file = open('engmix.txt')

word = input('Enter a word: ')

for line in file:
    if word == line:
        result = 'is'
    else:
        result = 'is not'
        
print('The word', result, 'in the dictionary')
