//! Dinic's max flow algorithm in Rust.

pub struct Dinic {
    adj: Vec<Vec<usize>>,
    to: Vec<usize>,
    cap: Vec<i64>,
    dist: Vec<i64>,
    ptr: Vec<usize>,
}

impl Dinic {
    pub fn new(n: usize) -> Self {
        Dinic {
            adj: vec![vec![]; n],
            to: Vec::new(),
            cap: Vec::new(),
            dist: vec![0; n],
            ptr: vec![0; n],
        }
    }

    pub fn add_edge(&mut self, u: usize, v: usize, c: i64) {
        self.adj[u].push(self.to.len());
        self.to.push(v);
        self.cap.push(c);
        self.adj[v].push(self.to.len());
        self.to.push(u);
        self.cap.push(0);
    }

    fn bfs(&mut self, s: usize, t: usize) -> bool {
        self.dist.fill(-1);
        self.dist[s] = 0;
        let mut q = std::collections::VecDeque::from([s]);
        while let Some(u) = q.pop_front() {
            for &eid in &self.adj[u] {
                let v = self.to[eid];
                if self.dist[v] == -1 && self.cap[eid] > 0 {
                    self.dist[v] = self.dist[u] + 1;
                    q.push_back(v);
                }
            }
        }
        self.dist[t] != -1
    }

    fn dfs(&mut self, u: usize, t: usize, f: i64) -> i64 {
        if u == t || f == 0 {
            return f;
        }
        while self.ptr[u] < self.adj[u].len() {
            let eid = self.adj[u][self.ptr[u]];
            let v = self.to[eid];
            if self.dist[v] == self.dist[u] + 1 && self.cap[eid] > 0 {
                let pushed = self.dfs(v, t, f.min(self.cap[eid]));
                if pushed > 0 {
                    self.cap[eid] -= pushed;
                    self.cap[eid ^ 1] += pushed;
                    return pushed;
                }
            }
            self.ptr[u] += 1;
        }
        0
    }

    pub fn max_flow(&mut self, s: usize, t: usize) -> i64 {
        let mut flow = 0;
        while self.bfs(s, t) {
            self.ptr.fill(0);
            loop {
                let f = self.dfs(s, t, i64::MAX);
                if f == 0 {
                    break;
                }
                flow += f;
            }
        }
        flow
    }
}

fn main() {
    let mut d = Dinic::new(6);
    d.add_edge(0, 1, 16);
    d.add_edge(0, 2, 13);
    d.add_edge(1, 2, 10);
    d.add_edge(1, 3, 12);
    d.add_edge(2, 1, 4);
    d.add_edge(2, 4, 14);
    d.add_edge(3, 2, 9);
    d.add_edge(3, 5, 20);
    d.add_edge(4, 3, 7);
    d.add_edge(4, 5, 4);
    assert_eq!(d.max_flow(0, 5), 23);
    println!("[Rust Dinic] Max flow verified: 23");
}
