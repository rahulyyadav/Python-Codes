n = int(input())
l = list(map(int, input().split()))

res = [0] * n

for i in range(n):
	for j in range(n):
		if l[j] == i+1:
			res[i] = j + 1
			break

print(" ".join(map(str, res)))