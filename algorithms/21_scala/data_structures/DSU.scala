object DSU {
  class UnionFind(n: Int) {
    private val parent = (0 until n).toArray
    private val rank = Array.fill(n)(0)

    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }

    def union(x: Int, y: Int): Unit = {
      val rx = find(x)
      val ry = find(y)
      if (rx == ry) return
      if (rank(rx) < rank(ry)) parent(rx) = ry
      else if (rank(rx) > rank(ry)) parent(ry) = rx
      else { parent(ry) = rx; rank(rx) += 1 }
    }

    def connected(x: Int, y: Int): Boolean = find(x) == find(y)
  }

  def main(args: Array[String]): Unit = {
    val dsu = new UnionFind(5)
    dsu.union(0, 1)
    dsu.union(1, 2)
    dsu.union(3, 4)
    assert(dsu.connected(0, 2), "union failed")
    assert(!dsu.connected(0, 3), "spurious union")
    println("[Scala DSU] Disjoint set union verified")
  }
}
