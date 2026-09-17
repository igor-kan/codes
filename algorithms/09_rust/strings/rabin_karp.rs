pub fn rabin_karp(text: &str, pat: &str) -> Vec<usize> {
    let mut matches = Vec::new();
    if pat.is_empty() || pat.len() > text.len() { return matches; }
    let n = text.len();
    let m = pat.len();
    let d = 256;
    let q = 1000000007;
    let mut h = 1;
    for _ in 0..m - 1 { h = (h * d) % q; }
    let mut p_hash = 0;
    let mut t_hash = 0;
    let t_bytes = text.as_bytes();
    let p_bytes = pat.as_bytes();
    for i in 0..m {
        p_hash = (d * p_hash + p_bytes[i] as i64) % q;
        t_hash = (d * t_hash + t_bytes[i] as i64) % q;
    }
    for i in 0..=n - m {
        if p_hash == t_hash && &text[i..i + m] == pat { matches.push(i); }
        if i < n - m {
            t_hash = (d * (t_hash - t_bytes[i] as i64 * h) + t_bytes[i + m] as i64) % q;
            if t_hash < 0 { t_hash += q; }
        }
    }
    matches
}
fn main() {
    let m = rabin_karp("AABAACAADAABAABA", "AABA");
    assert_eq!(m, vec![0, 9, 12]);
    println!("Rust Rabin-Karp verified.");
}
