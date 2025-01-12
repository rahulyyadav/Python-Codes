n = int(input())
money = [100, 20, 10, 5, 1]
count = 0

for l in money:
	count += n // l
	n %= l

print(count)