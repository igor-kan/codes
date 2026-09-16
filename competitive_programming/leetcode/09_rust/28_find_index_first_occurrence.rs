fn str_str(haystack: &str, needle: &str) -> i32 {
    match haystack.find(needle) {
        Some(position) => position as i32,
        None => -1,
    }
}

fn main() {
    assert_eq!(str_str("sadbutsad", "sad"), 0);
    assert_eq!(str_str("leetcode", "leeto"), -1);
    println!("28 find index first occurrence ok");
}
