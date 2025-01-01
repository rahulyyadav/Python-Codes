username = input()
hashmap = {}

if len(username) <= 100:
	for c in username:
		if c in hashmap:
			pass
		else:
			hashmap[c] = 1

count = sum(hashmap.values())

if count%2 == 0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")