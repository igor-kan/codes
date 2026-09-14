class DSU(private val n: Int) {
    private val parent = IntArray(n) { it }
    private val rank = IntArray(n)

    fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }

    fun union(x: Int, y: Int) {
        val rx = find(x)
        val ry = find(y)
        if (rx == ry) return
        when {
            rank[rx] < rank[ry] -> parent[rx] = ry
            rank[rx] > rank[ry] -> parent[ry] = rx
            else -> { parent[ry] = rx; rank[rx]++ }
        }
    }

    fun connected(x: Int, y: Int) = find(x) == find(y)
}

fun main() {
    val dsu = DSU(5)
    dsu.union(0, 1)
    dsu.union(1, 2)
    dsu.union(3, 4)
    check(dsu.connected(0, 2))
    check(!dsu.connected(0, 3))
    println("[Kotlin DSU] Disjoint set union verified")
}
