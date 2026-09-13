//! Topological Sort (Kahn's Algorithm) in Rust.

use std::collections::VecDeque;

pub fn kahns_topological_sort(n: usize, edges: &[(usize, usize)]) -> Option<Vec<usize>> {
    let mut adj = vec![vec![]; n];
    let mut in_degree = vec![0; n];

    for &(u, v) in edges {
        adj[u].push(v);
        in_degree[v] += 1;
    }

    let mut q: VecDeque<usize> = in_degree.iter().enumerate()
        .filter_map(|(i, &deg)| if deg == 0 { Some(i) } else { None })
        .collect();

    let mut order = Vec::with_capacity(n);

    while let Some(u) = q.pop_front() {
        order.push(u);
        for &v in &adj[u] {
            in_degree[v] -= 1;
            if in_degree[v] == 0 {
                q.push_back(v);
            }
        }
    }

    if order.len() == n {
        Some(order)
    } else {
        None // Cycle detected
    }
}

fn main() {
    let edges = vec![
        (5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)
    ];
    let n = 6;
    let order = kahns_topological_sort(n, &edges).expect("Graph is a DAG");
    assert_eq!(order.len(), n);

    let mut pos = vec![0; n];
    for (i, &node) in order.iter().enumerate() {
        pos[node] = i;
    }
    for &(u, v) in &edges {
        assert!(pos[u] < pos[v]);
    }

    println!("[Rust TopoSort] Valid DAG order verified: {:?}", order);
}
