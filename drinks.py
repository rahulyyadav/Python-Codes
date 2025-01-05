n = int(input())
drinks = list(map(int, input().split()))
toj = 0

for i in range(n):
	toj += float(drinks[i]/100)


result = (toj/n)*100
print(result)