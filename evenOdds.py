nums = list(map(int, input().split()))
n, k = nums[0], nums[1]

totalOdds = (n + 1) // 2

if k <= totalOdds:

	result = 2 * k - 1
else:
	result = 2 * (k - totalOdds)

print(result)