
file = open('mateo.txt', 'r')
words = file.readlines()
for line in words:
    print(line)
file.close()
