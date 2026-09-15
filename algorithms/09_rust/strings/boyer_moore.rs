//! Boyer-Moore-Horspool substring search.
fn boyer_moore(text: &[u8], pat: &[u8]) -> Option<usize> {
    let n = text.len();
    let m = pat.len();
    if m > n {
        return None;
    }
    let mut skip = [m; 256];
    for i in 0..m.saturating_sub(1) {
        skip[pat[i] as usize] = m - 1 - i;
    }
    let mut i = 0;
    while i + m <= n {
        let mut j = m;
        loop {
            if j == 0 {
                return Some(i);
            }
            if text[i + j - 1] != pat[j - 1] {
                break;
            }
            j -= 1;
        }
        i += skip[text[i + m - 1] as usize];
    }
    None
}

fn main() {
    assert_eq!(boyer_moore(b"here is a simple example", b"example"), Some(17));
    assert_eq!(boyer_moore(b"abc", b"xyz"), None);
    println!("boyer-moore ok");
}
