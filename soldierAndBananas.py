inp = list(map(int, str(input()).split(" ")))

Price = inp[0]   #3
amountIhave = inp[1]  #17
ToBuy = inp[2]        #4
amountIreq = 0

for i in range(1,ToBuy+1):
	amountIreq += Price * i

borrow = max(0, amountIreq - amountIhave)
print(borrow)