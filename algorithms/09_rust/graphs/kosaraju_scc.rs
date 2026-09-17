//! Kosaraju's SCC Algorithm (CLRS 3rd Ed. Chapter 22.5)
//! Two-pass DFS on graph and transpose graph.

pub fn kosaraju(n: usize, adj: &[Vec<usize>]) -> Vec<Vec<usize>> {
    let mut visited = vec![false; n];
    let mut order = Vec::new();

    fn dfs1(u: usize, adj: &[Vec<usize>], vis: &mut [bool], order: &mut Vec<usize>) {
        vis[u] = true;
        for &v in &adj[u] {
            if !vis[v] {
                dfs1(v, adj, vis, order);
            }
        }
        order.push(u);
    }

    for i in 0..n {
        if !visited[i] {
            dfs1(i, adj, &mut visited, &mut order);
        }
    }

    let mut rev_adj = vec![Vec::new(); n];
    for u in 0..n {
        for &v in &adj[u] {
            rev_adj[v].push(u);
        }
    }

    visited.fill(false);
    let mut sccs = Vec::new();

    fn dfs2(u: usize, rev: &[Vec<usize>], vis: &mut [bool], comp: &mut Vec<usize>) {
        vis[u] = true;
        comp.push(u);
        for &v in &rev[u] {
            if !vis[v] {
                dfs2(v, rev, vis, comp);
            }
        }
    }

    while let Some(u) = order.pop() {
        if !visited[u] {
            let mut comp = Vec::new();
            dfs2(u, &rev_adj, &mut visited, &mut comp);
            sccs.push(comp);
        }
    }
    sccs
}

fn main() {
    let adj = vec![vec![1], vec![2], vec![0, 3], vec![4], vec![3]];
    let sccs = kosaraju(5, &adj);
    assert_eq!(sccs.len(), 2);
    println!("Rust Kosaraju SCC verified.");
}
