# python3
import sys
from collections import defaultdict, deque

def algo():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    graph = [[] for _ in range(n)]
    in_deg = [0]*n
    out_deg = [0]*n
    
    for i in range(m):
        u = int(data[2+2*i]) - 1
        v = int(data[3+2*i]) - 1
        graph[u].append(v)
        out_deg[u] += 1
        in_deg[v] += 1

    if any(in_deg[i] != out_deg[i] for i in range(n)):
        print(0)
        return

    stack = [0]
    path = []
    graph_iter = [deque(adj) for adj in graph]

    while stack:
        u = stack[-1]
        if graph_iter[u]:
            v = graph_iter[u].popleft()
            stack.append(v)
        else:
            path.append(stack.pop())

    if len(path) - 1 != m:
        print(0)
    else:
        print(1)
        print(' '.join(str(node + 1) for node in reversed(path[:-1])))

if __name__ == "__main__":
    algo()