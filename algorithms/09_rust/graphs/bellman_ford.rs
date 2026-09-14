//! Bellman-Ford single-source shortest paths.
const INF: i64 = i64::MAX / 4;

#[derive(Clone, Copy)]
struct Edge {
    from: usize,
    to: usize,
    weight: i64,
}

fn bellman_ford(n: usize, edges: &[Edge], source: usize) -> Option<Vec<i64>> {
    let mut dist = vec![INF; n];
    dist[source] = 0;
    for _ in 0..n.saturating_sub(1) {
        for e in edges {
            if dist[e.from] != INF && dist[e.from] + e.weight < dist[e.to] {
                dist[e.to] = dist[e.from] + e.weight;
            }
        }
    }
    for e in edges {
        if dist[e.from] != INF && dist[e.from] + e.weight < dist[e.to] {
            return None;
        }
    }
    Some(dist)
}

fn main() {
    let edges = [
        Edge { from: 0, to: 1, weight: 4 },
        Edge { from: 0, to: 2, weight: 5 },
        Edge { from: 1, to: 2, weight: -3 },
        Edge { from: 2, to: 3, weight: 2 },
    ];
    let dist = bellman_ford(4, &edges, 0).expect("no negative cycle");
    assert_eq!(dist, vec![0, 4, 1, 3]);
    println!("{dist:?}");
}
