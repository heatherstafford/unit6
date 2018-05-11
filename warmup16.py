#Heather Stafford
#5/11/18
#warmup16.py

file = open('engmix.txt')

for line in file:
    if 'H' in line:
        print(line.strip())

