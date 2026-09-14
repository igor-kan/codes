//! Manacher's algorithm for longest palindromic substring in Rust.

pub fn manacher(s: &str) -> String {
    let bytes = s.as_bytes();
    let mut t: Vec<u8> = Vec::with_capacity(2 * bytes.len() + 1);
    t.push(b'#');
    for &c in bytes {
        t.push(c);
        t.push(b'#');
    }
    let n = t.len();
    let mut p = vec![0usize; n];
    let (mut c, mut r) = (0usize, 0usize);
    for i in 0..n {
        let mirror = 2 * c - i;
        if i < r {
            p[i] = p[mirror].min(r - i);
        }
        while i >= p[i] + 1 && i + p[i] + 1 < n && t[i - p[i] - 1] == t[i + p[i] + 1] {
            p[i] += 1;
        }
        if i + p[i] > r {
            c = i;
            r = i + p[i];
        }
    }
    let (mut center, mut max_len) = (0usize, 0usize);
    for i in 0..n {
        if p[i] > max_len {
            max_len = p[i];
            center = i;
        }
    }
    let start = (center - max_len) / 2;
    s[start..start + max_len].to_string()
}

fn main() {
    let babad = manacher("babad");
    assert!(babad == "bab" || babad == "aba");
    assert_eq!(manacher("cbbd"), "bb");
    assert_eq!(manacher("racecar"), "racecar");
    println!("[Rust Manacher] Longest palindromic substring verified.");
}
