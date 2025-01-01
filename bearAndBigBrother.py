weight = list(map(int, str(input()).split(" ")))
years = 0

if 1 <= weight[0] <= 10 and 1 <= weight[1] <= 10:
	while weight[0] <= weight[1]:
		weight[0] = weight[0]*3
		weight[1] = weight[1]*2
		years += 1

	print(years)