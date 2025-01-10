n = int(input())
l1 = list(map(int, input().split()))[1:]
l2 = list(map(int, input().split()))[1:]

res = set(l1 + l2)
exp = set(range(1, n + 1))

if exp.issubset(res):
	print("I become the guy.")
else:
	print("Oh, my keyboard!")



