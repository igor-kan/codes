// Dijkstra's Algorithm in Swift (CLRS 3rd Ed. Chapter 24.3)

struct Edge {
    let to: Int
    let weight: Double
}

func dijkstra(n: Int, adj: [[Edge]], source: Int) -> [Double] {
    var dist = [Double](repeating: .infinity, count: n)
    var visited = [Bool](repeating: false, count: n)
    dist[source] = 0.0

    for _ in 0..<n {
        var u = -1
        for i in 0..<n {
            if !visited[i] && (u == -1 || dist[i] < dist[u]) {
                u = i
            }
        }
        if dist[u] == .infinity { break }
        visited[u] = true

        for edge in adj[u] {
            if dist[u] + edge.weight < dist[edge.to] {
                dist[edge.to] = dist[u] + edge.weight
            }
        }
    }
    return dist
}

let adj = [
    [Edge(to: 1, weight: 4.0), Edge(to: 2, weight: 1.0)],
    [Edge(to: 3, weight: 1.0)],
    [Edge(to: 1, weight: 2.0), Edge(to: 3, weight: 5.0)],
    []
]
let d = dijkstra(n: 4, adj: adj, source: 0)
assert(d[3] == 4.0)
print("Swift Dijkstra verified.")
