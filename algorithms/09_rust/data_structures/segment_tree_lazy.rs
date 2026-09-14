//! Segment tree with lazy propagation (range add, range sum) in Rust.

pub struct LazySegTree {
    tree: Vec<i64>,
    lazy: Vec<i64>,
    n: usize,
}

impl LazySegTree {
    pub fn new(arr: &[i64]) -> Self {
        let n = arr.len();
        let mut st = LazySegTree {
            tree: vec![0; 4 * n],
            lazy: vec![0; 4 * n],
            n,
        };
        if n > 0 {
            st.build(1, 0, n - 1, arr);
        }
        st
    }

    fn build(&mut self, node: usize, lo: usize, hi: usize, arr: &[i64]) {
        if lo == hi {
            self.tree[node] = arr[lo];
            return;
        }
        let mid = (lo + hi) / 2;
        self.build(node * 2, lo, mid, arr);
        self.build(node * 2 + 1, mid + 1, hi, arr);
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1];
    }

    fn push(&mut self, node: usize, lo: usize, hi: usize) {
        if self.lazy[node] != 0 {
            self.tree[node] += (hi - lo + 1) as i64 * self.lazy[node];
            if lo != hi {
                self.lazy[node * 2] += self.lazy[node];
                self.lazy[node * 2 + 1] += self.lazy[node];
            }
            self.lazy[node] = 0;
        }
    }

    pub fn update(&mut self, l: usize, r: usize, val: i64) {
        self.update_rec(1, 0, self.n - 1, l, r, val);
    }

    fn update_rec(&mut self, node: usize, lo: usize, hi: usize, l: usize, r: usize, val: i64) {
        self.push(node, lo, hi);
        if r < lo || hi < l {
            return;
        }
        if l <= lo && hi <= r {
            self.lazy[node] += val;
            self.push(node, lo, hi);
            return;
        }
        let mid = (lo + hi) / 2;
        self.update_rec(node * 2, lo, mid, l, r, val);
        self.update_rec(node * 2 + 1, mid + 1, hi, l, r, val);
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1];
    }

    pub fn query(&mut self, l: usize, r: usize) -> i64 {
        self.query_rec(1, 0, self.n - 1, l, r)
    }

    fn query_rec(&mut self, node: usize, lo: usize, hi: usize, l: usize, r: usize) -> i64 {
        self.push(node, lo, hi);
        if r < lo || hi < l {
            return 0;
        }
        if l <= lo && hi <= r {
            return self.tree[node];
        }
        let mid = (lo + hi) / 2;
        self.query_rec(node * 2, lo, mid, l, r) + self.query_rec(node * 2 + 1, mid + 1, hi, l, r)
    }
}

fn main() {
    let arr = [1i64, 2, 3, 4, 5];
    let mut st = LazySegTree::new(&arr);
    assert_eq!(st.query(0, 4), 15);
    st.update(1, 3, 2); // [1, 4, 5, 6, 5]
    assert_eq!(st.query(0, 4), 21);
    assert_eq!(st.query(1, 3), 15);
    assert_eq!(st.query(2, 2), 5);
    println!("[Rust LazySegTree] Range add / range sum verified.");
}
