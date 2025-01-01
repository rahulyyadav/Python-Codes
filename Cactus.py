from collections import defaultdict, deque

MOD = 1000000007

def find_cycles_and_parents(n, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    cycle_membership = [-1] * (n + 1)  # -1 means not part of any cycle
    cycles = []
    
    def dfs(v):
        stack = [(v, -1)]
        path = []
        while stack:
            node, par = stack.pop()
            if visited[node]:
                # Cycle detected
                if cycle_membership[node] == -1:
                    cycle = []
                    idx = len(path) - 1
                    while path[idx] != node:
                        cycle.append(path[idx])
                        idx -= 1
                    cycle.append(node)
                    cycles.append(cycle)
                    for u in cycle:
                        cycle_membership[u] = len(cycles) - 1
                continue
            visited[node] = True
            parent[node] = par
            path.append(node)
            for neighbor in graph[node]:
                if neighbor != par:
                    stack.append((neighbor, node))
            while path and path[-1] != node:
                path.pop()
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    
    return graph, parent, cycle_membership, cycles

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n, m = map(int, data[idx:idx+2])
    idx += 2
    edges = [tuple(map(int, data[idx+i:idx+i+2])) for i in range(0, 2*m, 2)]
    idx += 2 * m
    k = int(data[idx])
    idx += 1
    queries = [tuple(map(int, data[idx+i:idx+i+2])) for i in range(0, 2*k, 2)]
    
    # Step 1: Find cycles and tree structure
    graph, parent, cycle_membership, cycles = find_cycles_and_parents(n, edges)
    
    # Step 2: Process queries
    results = []
    for x, y in queries:
        if cycle_membership[x] == cycle_membership[y]:
            # Both in the same cycle or neither is part of a cycle
            if cycle_membership[x] == -1:
                results.append(1)  # Tree path is unique
            else:
                # Calculate paths in the cycle
                cycle_id = cycle_membership[x]
                cycle = cycles[cycle_id]
                pos_x = cycle.index(x)
                pos_y = cycle.index(y)
                size = len(cycle)
                dist = abs(pos_x - pos_y)
                results.append((dist + size - dist) % MOD)
        else:
            results.append(1)  # Tree path is unique
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")
