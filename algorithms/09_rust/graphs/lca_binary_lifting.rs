//! Lowest Common Ancestor via binary lifting in Rust.

pub struct LCA {
    up: Vec<Vec<usize>>,
    depth: Vec<usize>,
    log: usize,
}

impl LCA {
    pub fn new(adj: &[Vec<usize>], root: usize) -> Self {
        let n = adj.len();
        let mut log = 0;
        while (1 << log) <= n {
            log += 1;
        }
        let mut up = vec![vec![0usize; log]; n];
        let mut depth = vec![0usize; n];
        fn dfs(
            u: usize,
            p: usize,
            adj: &[Vec<usize>],
            up: &mut [Vec<usize>],
            depth: &mut [usize],
            log: usize,
        ) {
            up[u][0] = p;
            for k in 1..log {
                up[u][k] = up[up[u][k - 1]][k - 1];
            }
            for &v in &adj[u] {
                if v != p {
                    depth[v] = depth[u] + 1;
                    dfs(v, u, adj, up, depth, log);
                }
            }
        }
        dfs(root, root, adj, &mut up, &mut depth, log);
        LCA { up, depth, log }
    }

    pub fn query(&self, mut a: usize, mut b: usize) -> usize {
        if self.depth[a] < self.depth[b] {
            std::mem::swap(&mut a, &mut b);
        }
        let diff = self.depth[a] - self.depth[b];
        for k in 0..self.log {
            if diff & (1 << k) != 0 {
                a = self.up[a][k];
            }
        }
        if a == b {
            return a;
        }
        for k in (0..self.log).rev() {
            if self.up[a][k] != self.up[b][k] {
                a = self.up[a][k];
                b = self.up[b][k];
            }
        }
        self.up[a][0]
    }
}

fn main() {
    let adj = vec![
        vec![1, 2],
        vec![0, 3, 4],
        vec![0, 5, 6],
        vec![1],
        vec![1],
        vec![2],
        vec![2],
    ];
    let lca = LCA::new(&adj, 0);
    assert_eq!(lca.query(3, 4), 1);
    assert_eq!(lca.query(3, 6), 0);
    assert_eq!(lca.query(5, 6), 2);
    println!("[Rust LCA] Binary lifting verified.");
}
