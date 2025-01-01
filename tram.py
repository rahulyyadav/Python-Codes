n = int(input())
maxCap = 0
Cap = 0


for i in range(n):
	stope = list(map(int, str(input()).split(" ")))

	Cap = Cap - stope[0]
	Cap = Cap + stope[1]
	maxCap = max(maxCap, Cap)

print(maxCap)