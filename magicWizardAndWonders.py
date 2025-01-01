from collections import deque

def solve(n, d, limit):
    queue = deque([(i,) for i in range(1, limit + 1)])
    while queue:
        seq = queue.popleft()
        if len(seq) == n:
            if seq[-2] - seq[-1] == d:
                return seq
        else:
            for i in range(1, limit + 1):
                queue.append(seq + (i,))

    return [-1]

n, d, limit = map(int, input().split())
result = solve(n, d, limit)
print(*result)
