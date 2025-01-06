n1 = input()
n2 = input()
result = []

for i in range(len(n1)):
	if n1[i] == n2[i]:
		result.append(str(0))
	else:
		result.append(str(1))
print("".join(result))

