import string

n = int(input())
sen = str(input())

sentence = sen.lower()

alpha = set(string.ascii_lowercase)

sen_let = set(sentence)

if alpha.issubset(sen_let):
	print("YES")
else:
	print("NO")