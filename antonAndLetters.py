s = input()
if s =="{}":
	print(0)
else:
	print(len(set(set(s.strip("{}").replace(" ", "").split(",")))))