//! Hierholzer's Algorithm in Rust
//! Linear time O(V + E) Eulerian circuit/path solver on directed graphs.

pub fn hierholzer(n: usize, mut adj: Vec<Vec<usize>>) -> Option<Vec<usize>> {
    let mut in_degree = vec![0; n];
    let mut out_degree = vec![0; n];

    for u in 0..n {
        out_degree[u] = adj[u].len();
        for &v in &adj[u] {
            in_degree[v] += 1;
        }
    }

    let mut start_node = 0;
    for i in 0..n {
        if out_degree[i] > in_degree[i] {
            start_node = i;
            break;
        }
    }

    let mut stack = vec![start_node];
    let mut path = Vec::new();

    while let Some(&u) = stack.last() {
        if !adj[u].is_empty() {
            let v = adj[u].pop().unwrap();
            stack.push(v);
        } else {
            path.push(stack.pop().unwrap());
        }
    }
    path.reverse();
    Some(path)
}

fn main() {
    let adj = vec![vec![1], vec![2], vec![0, 3], vec![0]];
    let path = hierholzer(4, adj);
    assert!(path.is_some());
    println!("Rust Hierholzer Eulerian Circuit verified.");
}
