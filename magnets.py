n = int(input())
pre = []
count = 1

for i in range(n):
	s = str(input())

	if pre and s != pre[-1]:
		count += 1
	
	pre.append(s)
		
print(count)