package graphs

import java.util.PriorityQueue

data class Edge(val to: Int, val weight: Double)
data class NodeDist(val node: Int, val dist: Double) : Comparable<NodeDist> {
    override fun compareTo(other: NodeDist) = dist.compareTo(other.dist)
}

fun dijkstra(n: Int, adj: List<List<Edge>>, source: Int): DoubleArray {
    val dist = DoubleArray(n) { Double.POSITIVE_INFINITY }
    dist[source] = 0.0
    val pq = PriorityQueue<NodeDist>()
    pq.add(NodeDist(source, 0.0))

    while (pq.isNotEmpty()) {
        val (u, d) = pq.poll()
        if (d > dist[u]) continue
        for (edge in adj[u]) {
            if (dist[u] + edge.weight < dist[edge.to]) {
                dist[edge.to] = dist[u] + edge.weight
                pq.add(NodeDist(edge.to, dist[edge.to]))
            }
        }
    }
    return dist
}

fun main() {
    val adj = listOf(
        listOf(Edge(1, 4.0), Edge(2, 1.0)),
        listOf(Edge(3, 1.0)),
        listOf(Edge(1, 2.0), Edge(3, 5.0)),
        emptyList()
    )
    val d = dijkstra(4, adj, 0)
    assert(d[3] == 4.0)
    println("Kotlin Dijkstra verified.")
}
