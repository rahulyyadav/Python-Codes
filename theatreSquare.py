arr = list(map(int, str(input()).split(" ")))

toN = ((arr[0] + arr[2]) - 1) // arr[2]
toM = ((arr[1] + arr[2]) -1 ) // arr[2]

total = toN * toM

print(total)