//! Disjoint Set Union (path compression + union by size) in Rust.

pub struct DSU {
    parent: Vec<usize>,
    size: Vec<usize>,
}

impl DSU {
    pub fn new(n: usize) -> Self {
        DSU {
            parent: (0..n).collect(),
            size: vec![1; n],
        }
    }

    pub fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            self.parent[x] = self.find(self.parent[x]);
        }
        self.parent[x]
    }

    pub fn union(&mut self, a: usize, b: usize) -> bool {
        let (mut ra, mut rb) = (self.find(a), self.find(b));
        if ra == rb {
            return false;
        }
        if self.size[ra] < self.size[rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        self.size[ra] += self.size[rb];
        true
    }
}

fn main() {
    let mut d = DSU::new(6);
    assert!(d.union(0, 1));
    assert!(d.union(1, 2));
    assert!(d.union(3, 4));
    assert_eq!(d.find(0), d.find(2));
    assert_ne!(d.find(0), d.find(3));
    let root0 = d.find(0);
    assert_eq!(d.size[root0], 3);
    println!("[Rust DSU] Path compression + union by size verified.");
}
