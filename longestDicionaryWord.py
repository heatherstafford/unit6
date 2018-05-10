#Heather Stafford
#5/10/18
#longestDictionaryWord.py

file = open('engmix.txt')

longest = 0
word = ' '

for item in file:
    if len(item) > longest:
        longest = len(item)
        word = item
print('The longest word is', word)
