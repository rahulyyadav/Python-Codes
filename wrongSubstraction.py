numbers = list(map(str, str(input()).split(" ")))

for i in range(int(numbers[1])):
	if int(numbers[0][-1]) != 0:
		numbers[0] = str(int(numbers[0])-1)
	else:
		numbers[0] = str(int(numbers[0])//10)
print(int(numbers[0]))