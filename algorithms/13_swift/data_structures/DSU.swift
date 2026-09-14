final class DSU {
    private var parent: [Int]
    private var rank: [Int]

    init(_ n: Int) {
        parent = Array(0..<n)
        rank = Array(repeating: 0, count: n)
    }

    func find(_ x: Int) -> Int {
        if parent[x] != x { parent[x] = find(parent[x]) }
        return parent[x]
    }

    func union(_ x: Int, _ y: Int) {
        let rx = find(x), ry = find(y)
        if rx == ry { return }
        if rank[rx] < rank[ry] {
            parent[rx] = ry
        } else if rank[rx] > rank[ry] {
            parent[ry] = rx
        } else {
            parent[ry] = rx
            rank[rx] += 1
        }
    }

    func connected(_ x: Int, _ y: Int) -> Bool { find(x) == find(y) }
}

let dsu = DSU(5)
dsu.union(0, 1)
dsu.union(1, 2)
dsu.union(3, 4)
assert(dsu.connected(0, 2))
assert(!dsu.connected(0, 3))
print("[Swift DSU] Disjoint set union verified")
