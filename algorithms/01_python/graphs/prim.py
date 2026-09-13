import heapq

def prim(graph, start=0):
    visited = set()
    heap = [(0, start, -1)]
    mst = []
    total = 0
    while heap:
        w, u, parent = heapq.heappop(heap)
        if u in visited: continue
        visited.add(u)
        if parent != -1:
            mst.append((parent, u, w))
            total += w
        for v, wt in graph.get(u, []):
            if v not in visited:
                heapq.heappush(heap, (wt, v, u))
    return mst, total
