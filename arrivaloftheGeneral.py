n = int(input())
heights = list(map(int, input().split()))

maxh = max(heights)
minh = min(heights)

maxI = heights.index(maxh)      
minI = len(heights) - 1 - heights[::-1].index(minh)  # rightmost min

swaps = maxI + ((n-1) - minI)
if maxI > minI:
    swaps -= 1

print(swaps)