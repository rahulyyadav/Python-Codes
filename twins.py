n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse = True)
forme = coins[0]
count = 1
forhim = 0

for i in range(1, n):
	forhim += coins[i]

for i in range(1, n):
	if forme <= forhim:
		forme += coins[i]
		count += 1
		forhim -= coins[i]
print(count)
