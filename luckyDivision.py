def isAlmostLucky(n):

	def is_lucky(number):
		return all(c in "47" for c in str(number))

	for i in range(1, n+1):
		if is_lucky(i) and n % i == 0:
			return "YES"
	return "NO"


n = int(input().strip())
print(isAlmostLucky(n))
