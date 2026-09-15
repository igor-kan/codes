fn petya_and_strings(a: &str, b: &str) -> i32 {
    let left = a.to_lowercase();
    let right = b.to_lowercase();
    if left < right { -1 } else if left > right { 1 } else { 0 }
}

fn main() {
    assert_eq!(petya_and_strings("aaaa", "aaaA"), 0);
    assert_eq!(petya_and_strings("abs", "Abz"), -1);
    assert_eq!(petya_and_strings("abcdefg", "AbCdEfF"), 1);
    println!("112A petya and strings ok");
}
