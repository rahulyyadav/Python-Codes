def max_occurrences(n, k, arr):
    arr.sort()
    prefix_sum = [0] * (n + 1)
    
    # Compute prefix sum
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    
    max_freq = 1
    best_number = arr[0]
    
    for i in range(n):
        # Binary search on the length of the group
        left, right = 1, i + 1
        while left <= right:
            mid = (left + right) // 2
            # Cost to make arr[i] appear `mid` times
            cost = arr[i] * mid - (prefix_sum[i + 1] - prefix_sum[i + 1 - mid])
            if cost <= k:
                if mid > max_freq:
                    max_freq = mid
                    best_number = arr[i]
                elif mid == max_freq:
                    best_number = min(best_number, arr[i])
                left = mid + 1
            else:
                right = mid - 1
    
    return max_freq, best_number

# Input handling
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Solve and output the result
result = max_occurrences(n, k, arr)
print(result[0], result[1])