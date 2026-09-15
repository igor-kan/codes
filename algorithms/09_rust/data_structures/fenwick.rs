//! Fenwick tree for prefix sums.
struct Fenwick {
    tree: Vec<i64>,
}

impl Fenwick {
    fn new(size: usize) -> Self {
        Fenwick { tree: vec![0; size + 1] }
    }
    fn add(&mut self, mut index: usize, delta: i64) {
        index += 1;
        while index < self.tree.len() {
            self.tree[index] += delta;
            index += index & index.wrapping_neg();
        }
    }
    fn prefix_sum(&self, mut index: usize) -> i64 {
        index += 1;
        let mut total = 0;
        while index > 0 {
            total += self.tree[index];
            index -= index & index.wrapping_neg();
        }
        total
    }
    fn range_sum(&self, left: usize, right: usize) -> i64 {
        self.prefix_sum(right) - if left == 0 { 0 } else { self.prefix_sum(left - 1) }
    }
}

fn main() {
    let mut tree = Fenwick::new(8);
    for (i, value) in [1, 3, 5, 7, 9, 11].iter().enumerate() {
        tree.add(i, *value);
    }
    assert_eq!(tree.prefix_sum(3), 16);
    assert_eq!(tree.range_sum(2, 4), 21);
    println!("fenwick tree ok");
}
