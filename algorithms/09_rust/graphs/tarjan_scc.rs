//! Tarjan's SCC Algorithm in Rust
//! Discovers all strongly connected components in directed graph in linear O(V + E) time.

pub struct Tarjan {
    adj: Vec<Vec<usize>>,
    index: Vec<i32>,
    lowlink: Vec<i32>,
    on_stack: Vec<bool>,
    stack: Vec<usize>,
    sccs: Vec<Vec<usize>>,
    timer: i32,
}

impl Tarjan {
    pub fn new(n: usize, adj: Vec<Vec<usize>>) -> Self {
        Tarjan {
            adj,
            index: vec![-1; n],
            lowlink: vec![-1; n],
            on_stack: vec![false; n],
            stack: Vec::new(),
            sccs: Vec::new(),
            timer: 0,
        }
    }

    pub fn run(&mut self) -> Vec<Vec<usize>> {
        for i in 0..self.index.len() {
            if self.index[i] == -1 {
                self.dfs(i);
            }
        }
        self.sccs.clone()
    }

    fn dfs(&mut self, u: usize) {
        self.index[u] = self.timer;
        self.lowlink[u] = self.timer;
        self.timer += 1;
        self.stack.push(u);
        self.on_stack[u] = true;

        for &v in &self.adj[u].clone() {
            if self.index[v] == -1 {
                self.dfs(v);
                self.lowlink[u] = self.lowlink[u].min(self.lowlink[v]);
            } else if self.on_stack[v] {
                self.lowlink[u] = self.lowlink[u].min(self.index[v]);
            }
        }

        if self.lowlink[u] == self.index[u] {
            let mut scc = Vec::new();
            while let Some(w) = self.stack.pop() {
                self.on_stack[w] = false;
                scc.push(w);
                if w == u {
                    break;
                }
            }
            self.sccs.push(scc);
        }
    }
}

fn main() {
    let adj = vec![vec![1], vec![2], vec![0, 3], vec![4], vec![5], vec![3]];
    let mut tarjan = Tarjan::new(6, adj);
    let sccs = tarjan.run();
    assert_eq!(sccs.len(), 2);
    println!("Rust Tarjan SCC verified.");
}
