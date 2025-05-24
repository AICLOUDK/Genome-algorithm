# python3
import sys

def algo(k):
    adj = {}
    for i in range(2**k):
        curr = bin(i)[2:].zfill(k)
        if curr != '1'*(k-1) and curr != '0'*k:
            prefix = curr[:-1]
            suffix = curr[1:]
            adj.setdefault(prefix, []).append(suffix)
            adj.setdefault(suffix, []).append(prefix)
    return adj

def algort(k, adj):
    start = '0'*(k-1)
    path = []
    stack = [start]
    while stack:
        v = stack[-1]
        if v in adj and adj[v]:
            w = adj[v].pop()
            adj[w].remove(v)
            stack.append(w)
        else:
            path.append(stack.pop())
    return path[::-1]

def print_k_mer(path):
    res = path[0]
    for p in path[1:]:
        res += p[-1]
    print(res)

if __name__ == "__main__":
    n = int(sys.stdin.read().strip())
    edges = algo(n)
    paths = algort(n, edges)
    print_k_mer(paths)