# python3
import sys
from collections import defaultdict
from heapq import heappop, heappush

class Edge:
    def __init__(self, u, v, capacity, bound):
        self.u, self.v, self.capacity, self.bound = u, v, capacity, bound
        self.diff = capacity - bound
        self.flow = 0

class FlowGraph:
    def __init__(self, n):
        self.edges = []
        self.graph = [[] for _ in range(n + 2)]
        self.deg_ver = [0] * (n + 2)
        self.D = 0

    def add_edge(self, u, v, bound, cap):
        e = Edge(u, v, cap, bound)
        rev = Edge(v, u, 0, 0)
        self.graph[u].append(len(self.edges))
        self.edges.append(e)
        self.graph[v].append(len(self.edges))
        self.edges.append(rev)
        self.deg_ver[u] += bound
        self.deg_ver[v] -= bound

def read_data():
    n, m = map(int, sys.stdin.readline().split())
    g = FlowGraph(n)
    for _ in range(m):
        u, v, b, c = map(int, sys.stdin.readline().split())
        g.add_edge(u - 1, v - 1, b, c)
    for v in range(n):
        if g.deg_ver[v] < 0:
            g.add_edge(n, v, 0, -g.deg_ver[v])
        elif g.deg_ver[v] > 0:
            g.add_edge(v, n + 1, 0, g.deg_ver[v])
            g.D += g.deg_ver[v]
    return g, n, m

def bfs(g, s, t):
    dist = [float('inf')] * len(g.graph)
    dist[s] = 0
    prev = [None] * len(g.graph)
    heap = [(0, s)]
    while heap:
        d, u = heappop(heap)
        if dist[u] < d:
            continue
        for i in g.graph[u]:
            e = g.edges[i]
            if e.diff > 0 and dist[e.v] > dist[u] + 1:
                dist[e.v] = dist[u] + 1
                prev[e.v] = i
                heappush(heap, (dist[e.v], e.v))
    if dist[t] == float('inf'):
        return False, []
    path = []
    v = t
    min_cap = float('inf')
    while prev[v] is not None:
        i = prev[v]
        path.append(i)
        min_cap = min(min_cap, g.edges[i].diff)
        v = g.edges[i].u
    path.reverse()
    return True, (path, min_cap)

def max_flow(g, s, t):
    flow = 0
    while True:
        exists, result = bfs(g, s, t)
        if not exists:
            break
        path, cap = result
        for i in path:
            g.edges[i].flow += cap
            g.edges[i ^ 1].flow -= cap
            g.edges[i].diff -= cap
            g.edges[i ^ 1].diff += cap
        flow += cap
    return flow

def find_circulation(g, n, m):
    flow = max_flow(g, n, n + 1)
    if flow != g.D:
        return False, []
    flows = [g.edges[i * 2].flow + g.edges[i * 2].bound for i in range(m)]
    return True, flows

def main():
    g, n, m = read_data()
    is_possible, flows = find_circulation(g, n, m)
    if not is_possible:
        print("NO")
    else:
        print("YES")
        print("\n".join(map(str, flows)))

if __name__ == "__main__":
    main()