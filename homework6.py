

file = open('engmix.txt')

word = input('Enter a word: ')

for line in file:
    if word in line:
        print('The word is in the dictionary')
    else:
        print('The word is not in the dictionary')
