n = str(input())
count = 0

for i in n:
	if int(i) == 4 or int(i) == 7:
		count += 1
if all( c in '47' for c in str(count)):
	print("YES")
else:
	print("NO")