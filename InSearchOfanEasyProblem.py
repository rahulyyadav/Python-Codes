n = int(input())
decision = list(map(int, str(input()).split(" ")))
hard = 0

for i in range(n):
	if decision[i] == 1:
		hard += 1
if hard > 0:
	print("HARD")
else:
	print("EASY")