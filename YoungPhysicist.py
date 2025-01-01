n = int(input())
mainarr = []
x = 0
y = 0
z = 0

for _ in range(n):
	arr = list(map(int, str(input()).split(" ")))
	mainarr.append(arr)

for i in range(n):
	x += mainarr[i][0]
	y += mainarr[i][1]
	z += mainarr[i][2]

if x == 0 and y == 0 and z == 0:
	print("YES")
else:
	print("NO")
