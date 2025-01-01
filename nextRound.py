pL = list(map(int, str(input()).split(" ")))
arr = list(map(int, str(input()).split(" ")))

cutOF = arr[(pL[1]-1)]
count = 0

for score in arr:
	if score >= cutOF and score > 0:
		count += 1

print(count)

