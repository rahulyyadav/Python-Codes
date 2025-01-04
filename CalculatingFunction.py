n = int(input())

if n % 2 == 0:
	res = n//2
else:
	res = -(n+1)//2

print(res)