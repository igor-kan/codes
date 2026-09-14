//! Directed cycle detection (three-color DFS) in Rust.

pub fn has_cycle(n: usize, edges: &[(usize, usize)]) -> bool {
    let mut adj = vec![vec![]; n];
    for &(u, v) in edges {
        adj[u].push(v);
    }
    // 0 = white (unvisited), 1 = gray (in stack), 2 = black (done)
    let mut color = vec![0u8; n];
    fn dfs(u: usize, adj: &[Vec<usize>], color: &mut [u8]) -> bool {
        color[u] = 1;
        for &v in &adj[u] {
            if color[v] == 1 {
                return true;
            }
            if color[v] == 0 && dfs(v, adj, color) {
                return true;
            }
        }
        color[u] = 2;
        false
    }
    for s in 0..n {
        if color[s] == 0 && dfs(s, &adj, &mut color) {
            return true;
        }
    }
    false
}

fn main() {
    assert!(has_cycle(3, &[(0, 1), (1, 2), (2, 0)]));
    assert!(!has_cycle(4, &[(0, 1), (1, 2), (0, 2), (2, 3)]));
    println!("[Rust CycleDetection] Directed cycle detection verified.");
}
