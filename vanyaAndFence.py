nh = list(map(int, str(input()).split(" ")))
h = list(map(int, str(input()).split(" ")))
w = 0

for i in h:
	if i <= nh[1]:
		w += 1
	else:
		w += 2
print(w)