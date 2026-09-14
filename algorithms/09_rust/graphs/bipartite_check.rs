//! Bipartite graph check (two-coloring) in Rust.

use std::collections::VecDeque;

pub fn is_bipartite(n: usize, edges: &[(usize, usize)]) -> bool {
    let mut adj = vec![vec![]; n];
    for &(u, v) in edges {
        adj[u].push(v);
        adj[v].push(u);
    }
    let mut color = vec![-1i8; n];
    for s in 0..n {
        if color[s] != -1 {
            continue;
        }
        color[s] = 0;
        let mut q = VecDeque::from([s]);
        while let Some(u) = q.pop_front() {
            for &v in &adj[u] {
                if color[v] == -1 {
                    color[v] = color[u] ^ 1;
                    q.push_back(v);
                } else if color[v] == color[u] {
                    return false;
                }
            }
        }
    }
    true
}

fn main() {
    let square = vec![(0, 1), (0, 3), (1, 2), (2, 3)];
    assert!(is_bipartite(4, &square));
    let triangle = vec![(0, 1), (1, 2), (2, 0)];
    assert!(!is_bipartite(3, &triangle));
    println!("[Rust Bipartite] Two-coloring check verified.");
}
