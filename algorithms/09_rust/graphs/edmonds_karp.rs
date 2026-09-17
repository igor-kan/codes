//! Edmonds-Karp Max Flow (CLRS 3rd Ed. Chapter 26.2)
//! Ford-Fulkerson method with BFS shortest augmenting paths.

pub struct EdmondsKarp {
    n: usize,
    capacity: Vec<Vec<i32>>,
}

impl EdmondsKarp {
    pub fn new(n: usize) -> Self {
        EdmondsKarp {
            n,
            capacity: vec![vec![0; n]; n],
        }
    }

    pub fn add_edge(&mut self, u: usize, v: usize, cap: i32) {
        self.capacity[u][v] += cap;
    }

    pub fn max_flow(&mut self, s: usize, t: usize) -> i32 {
        let mut flow = 0;
        let mut parent = vec![usize::MAX; self.n];

        while self.bfs(s, t, &mut parent) {
            let mut push = i32::MAX;
            let mut curr = t;
            while curr != s {
                let prev = parent[curr];
                push = push.min(self.capacity[prev][curr]);
                curr = prev;
            }

            curr = t;
            while curr != s {
                let prev = parent[curr];
                self.capacity[prev][curr] -= push;
                self.capacity[curr][prev] += push;
                curr = prev;
            }
            flow += push;
        }
        flow
    }

    fn bfs(&self, s: usize, t: usize, parent: &mut [usize]) -> bool {
        parent.fill(usize::MAX);
        parent[s] = s;
        let mut queue = std::collections::VecDeque::new();
        queue.push_back(s);

        while let Some(u) = queue.pop_front() {
            for v in 0..self.n {
                if parent[v] == usize::MAX && self.capacity[u][v] > 0 {
                    parent[v] = u;
                    if v == t {
                        return true;
                    }
                    queue.push_back(v);
                }
            }
        }
        false
    }
}

fn main() {
    let mut ek = EdmondsKarp::new(4);
    ek.add_edge(0, 1, 10);
    ek.add_edge(0, 2, 10);
    ek.add_edge(1, 2, 2);
    ek.add_edge(1, 3, 10);
    ek.add_edge(2, 3, 10);
    assert_eq!(ek.max_flow(0, 3), 20);
    println!("Rust Edmonds-Karp verified.");
}
