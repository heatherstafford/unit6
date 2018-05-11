#Heather Stafford
#5/11/18
#warmup16.py

file = open('engmix.txt')

for line in file:
    word = line.strip()
    if len(word)>0 and word[0] == 'h' and word[-1] == 's':
        print(word)
