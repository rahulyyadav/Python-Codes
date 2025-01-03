n = int(input())
count = 0

for i in range(n):
	room = list(map(int, str(input()).split(" ")))

	if room[0] < room[1] and (room[1] - room[0]) >= 2:
		count += 1

print(count)