

file = open('engmix.txt')

word = input('Enter a word: ')

if word in file:
    print('The word is in the dictionary')
else:
    print('The word is not in the dictionary')
