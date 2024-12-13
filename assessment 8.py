file = open('dictionaries.txt' , 'r')
words = file.read().split(" ")
file.close()
sdfsdf = {}

for word in words:
    sdfsdf[word] = sdfsdf.get(word,0) + 1

print(sdfsdf)
print = ('common_words(5)')

