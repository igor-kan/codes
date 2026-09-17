//! Hopcroft-Karp Algorithm in Rust
//! Maximum cardinality bipartite matching in O(E sqrt(V)).

pub struct HopcroftKarp {
    nu: usize,
    nv: usize,
    adj: Vec<Vec<usize>>,
    pair_u: Vec<usize>,
    pair_v: Vec<usize>,
    dist: Vec<usize>,
}

impl HopcroftKarp {
    pub fn new(nu: usize, nv: usize) -> Self {
        HopcroftKarp {
            nu,
            nv,
            adj: vec![Vec::new(); nu + 1],
            pair_u: vec![0; nu + 1],
            pair_v: vec![0; nv + 1],
            dist: vec![0; nu + 1],
        }
    }

    pub fn add_edge(&mut self, u: usize, v: usize) {
        self.adj[u].push(v);
    }

    pub fn max_matching(&mut self) -> usize {
        let mut matching = 0;
        while self.bfs() {
            for u in 1..=self.nu {
                if self.pair_u[u] == 0 && self.dfs(u) {
                    matching += 1;
                }
            }
        }
        matching
    }

    fn bfs(&mut self) -> bool {
        let mut queue = std::collections::VecDeque::new();
        for u in 1..=self.nu {
            if self.pair_u[u] == 0 {
                self.dist[u] = 0;
                queue.push_back(u);
            } else {
                self.dist[u] = usize::MAX;
            }
        }
        self.dist[0] = usize::MAX;

        while let Some(u) = queue.pop_front() {
            if self.dist[u] < self.dist[0] {
                for &v in &self.adj[u] {
                    if self.dist[self.pair_v[v]] == usize::MAX {
                        self.dist[self.pair_v[v]] = self.dist[u] + 1;
                        queue.push_back(self.pair_v[v]);
                    }
                }
            }
        }
        self.dist[0] != usize::MAX
    }

    fn dfs(&mut self, u: usize) -> bool {
        if u != 0 {
            for &v in &self.adj[u].clone() {
                if self.dist[self.pair_v[v]] == self.dist[u] + 1 && self.dfs(self.pair_v[v]) {
                    self.pair_v[v] = u;
                    self.pair_u[u] = v;
                    return true;
                }
            }
            self.dist[u] = usize::MAX;
            return false;
        }
        true
    }
}

fn main() {
    let mut hk = HopcroftKarp::new(4, 4);
    hk.add_edge(1, 2);
    hk.add_edge(1, 3);
    hk.add_edge(2, 1);
    hk.add_edge(3, 2);
    hk.add_edge(4, 2);
    hk.add_edge(4, 4);
    assert_eq!(hk.max_matching(), 4);
    println!("Rust Hopcroft-Karp verified.");
}
