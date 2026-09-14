//! Knuth-Morris-Pratt (KMP) String Search Algorithm in Rust.

pub fn compute_lps(pattern: &[u8]) -> Vec<usize> {
    let m = pattern.len();
    let mut lps = vec![0; m];
    let mut len = 0;
    let mut i = 1;

    while i < m {
        if pattern[i] == pattern[len] {
            len += 1;
            lps[i] = len;
            i += 1;
        } else if len != 0 {
            len = lps[len - 1];
        } else {
            lps[i] = 0;
            i += 1;
        }
    }
    lps
}

pub fn kmp_search(text: &str, pattern: &str) -> Vec<usize> {
    let t_bytes = text.as_bytes();
    let p_bytes = pattern.as_bytes();
    let (n, m) = (t_bytes.len(), p_bytes.len());

    if m == 0 || n == 0 {
        return vec![];
    }

    let lps = compute_lps(p_bytes);
    let mut occurrences = Vec::new();

    let mut i = 0;
    let mut j = 0;

    while i < n {
        if t_bytes[i] == p_bytes[j] {
            i += 1;
            j += 1;
        }

        if j == m {
            occurrences.push(i - j);
            j = lps[j - 1];
        } else if i < n && t_bytes[i] != p_bytes[j] {
            if j != 0 {
                j = lps[j - 1];
            } else {
                i += 1;
            }
        }
    }

    occurrences
}

fn main() {
    let txt = "ABABDABACDABABCABABABABCABAB";
    let pat = "ABABCABAB";
    let matches = kmp_search(txt, pat);

    assert_eq!(matches, vec![10, 19]);
    println!("[Rust KMP] Pattern matched at offsets: {:?}", matches);
}
