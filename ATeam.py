l = int(input())

count = 0

for _ in range(l):
	arr = list(map(int, input().split()))

	if arr.count(1) >= 2:
		count +=1

print(count)