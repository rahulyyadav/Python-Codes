inStr = input()

vowels = {"A", "O", "Y", "E", "U", "I"}
result = []


for c in inStr:
	if c.upper() not in vowels:
		result.append("." + c.lower())

fresult = "".join(result)
print(fresult)
