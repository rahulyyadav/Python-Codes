str1 = input().strip()
str2 = input().strip()

str1 = str1.lower()
str2 = str2.lower()

if str1 < str2:
	print("-1")
elif str2 < str1:
	print("1")
else:
	print("0")