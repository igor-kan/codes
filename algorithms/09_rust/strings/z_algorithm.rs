//! Z-algorithm in Rust.

pub fn z_algorithm(s: &[u8]) -> Vec<usize> {
    let n = s.len();
    let mut z = vec![0usize; n];
    let (mut l, mut r) = (0usize, 0usize);
    for i in 1..n {
        if i <= r {
            if z[i - l] < r - i + 1 {
                z[i] = z[i - l];
                continue;
            }
            z[i] = r - i + 1;
        }
        while i + z[i] < n && s[z[i]] == s[i + z[i]] {
            z[i] += 1;
        }
        if i + z[i] - 1 > r {
            l = i;
            r = i + z[i] - 1;
        }
    }
    z
}

fn main() {
    let s = b"aaaa";
    assert_eq!(z_algorithm(s), vec![0, 3, 2, 1]);
    let s2 = b"ababab";
    assert_eq!(z_algorithm(s2), vec![0, 0, 4, 0, 2, 0]);
    println!("[Rust ZAlgorithm] Z-values verified.");
}
