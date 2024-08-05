name = input()
words = name.split("-")
for word in words: 
    print (word[0].upper(), end="")
