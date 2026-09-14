//! Sparse Table for Range Minimum Query in Rust.

pub struct SparseTable {
    st: Vec<Vec<i64>>,
    log: Vec<usize>,
}

impl SparseTable {
    pub fn new(arr: &[i64]) -> Self {
        let n = arr.len();
        let mut log = vec![0usize; n + 1];
        for i in 2..=n {
            log[i] = log[i / 2] + 1;
        }
        let k = log[n] + 1;
        let mut st = vec![vec![0i64; k]; n];
        for i in 0..n {
            st[i][0] = arr[i];
        }
        for j in 1..k {
            let mut i = 0;
            while i + (1 << j) <= n {
                st[i][j] = st[i][j - 1].min(st[i + (1 << (j - 1))][j - 1]);
                i += 1;
            }
        }
        SparseTable { st, log }
    }

    pub fn query(&self, l: usize, r: usize) -> i64 {
        let j = self.log[r - l + 1];
        self.st[l][j].min(self.st[r - (1 << j) + 1][j])
    }
}

fn main() {
    let arr = [2i64, 5, 1, 4, 9, 3];
    let st = SparseTable::new(&arr);
    assert_eq!(st.query(0, 5), 1);
    assert_eq!(st.query(1, 3), 1);
    assert_eq!(st.query(4, 5), 3);
    assert_eq!(st.query(0, 0), 2);
    println!("[Rust SparseTable] Range minimum query verified.");
}
