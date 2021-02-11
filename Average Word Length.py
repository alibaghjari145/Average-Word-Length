text = input()

words=text.split()
wordslen=len(words)
letter=0
for l in words:
    letter+= len(l)

print(letter/wordslen)    