//! Counting sort in Rust.

pub fn counting_sort(a: &[usize], max_val: usize) -> Vec<usize> {
    let mut count = vec![0usize; max_val + 1];
    for &v in a {
        count[v] += 1;
    }
    for i in 1..=max_val {
        count[i] += count[i - 1];
    }
    let mut out = vec![0usize; a.len()];
    for &v in a.iter().rev() {
        count[v] -= 1;
        out[count[v]] = v;
    }
    out
}

fn main() {
    let data = [4usize, 2, 2, 8, 3, 3, 1];
    let sorted = counting_sort(&data, 8);
    assert_eq!(sorted, vec![1, 2, 2, 3, 3, 4, 8]);
    println!("[Rust CountingSort] Counting sort verified: {:?}", sorted);
}
