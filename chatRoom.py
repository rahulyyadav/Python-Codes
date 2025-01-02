s = str(input())
target = "hello"
p = 0

for c in s:
	if c == target[p]:
		p += 1
	if p == len(target):
		print("YES")
		break
else:
	print("NO")
