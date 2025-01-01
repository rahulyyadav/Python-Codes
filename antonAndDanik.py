n = int(input())
string = str(input())
countA = 0
countD = 0

for s in string:
	if s == "A":
		countA += 1
	else:
		countD += 1
if countA > countD:
	print("Anton")
elif countD > countA:
	print("Danik")
else:
	print("Friendship")