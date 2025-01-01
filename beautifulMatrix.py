mainarr = []

for _ in range(5):
	arr = list(map(int, str(input()).split(" ")))
	mainarr.append(arr)

coordinate = []

for row in range(len(mainarr)):
	for col in range(len(mainarr[row])):
		if mainarr[row][col] == 1:
			coordinate = [row+1, col+1]
			break

result = abs(coordinate[0]-3) + abs(coordinate[1] - 3)
print(result)

