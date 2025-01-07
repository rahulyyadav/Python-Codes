colors = list(map(int, input().split()))
hashmap = {}
count = 0

for i in colors: 
	if i in hashmap:
		count += 1
	else:
		hashmap[i] = 1
print(count)