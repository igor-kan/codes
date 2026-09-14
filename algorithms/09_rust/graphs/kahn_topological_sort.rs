//! Kahn's algorithm for topological sort in Rust.

use std::collections::VecDeque;

pub fn kahn_topological_sort(n: usize, edges: &[(usize, usize)]) -> Option<Vec<usize>> {
    let mut adj = vec![vec![]; n];
    let mut in_degree = vec![0usize; n];
    for &(u, v) in edges {
        adj[u].push(v);
        in_degree[v] += 1;
    }
    let mut q: VecDeque<usize> = in_degree
        .iter()
        .enumerate()
        .filter_map(|(i, &d)| if d == 0 { Some(i) } else { None })
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
        None
    }
}

fn main() {
    let edges = vec![(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)];
    let order = kahn_topological_sort(6, &edges).expect("graph is a DAG");
    let mut pos = vec![0usize; 6];
    for (i, &u) in order.iter().enumerate() {
        pos[u] = i;
    }
    for &(u, v) in &edges {
        assert!(pos[u] < pos[v]);
    }
    assert!(kahn_topological_sort(3, &[(0, 1), (1, 2), (2, 0)]).is_none());
    println!("[Rust Kahn] Topological sort verified: {:?}", order);
}
