def kruskal(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a == b: return False
        parent[a] = b
        return True
    mst = []
    for w, u, v in sorted(edges):
        if union(u, v):
            mst.append((u, v, w))
    return mst
