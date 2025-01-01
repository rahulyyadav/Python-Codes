y = int(input())

for sal in range(y+1, 10000):

	year = list(map(int, str(sal)))

	if len(year) == len(set(year)):
		print(sal)
		break