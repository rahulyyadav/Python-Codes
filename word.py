word = str(input())

countL = 0
countU = 0

for c in word: 
	if c.islower():
		countL += 1
	else:
		countU += 1

if countL > countU:
	print(word.lower())
elif countL == countU:
	print(word.lower())
else:
	print(word.upper())