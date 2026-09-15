fn watermelon(weight: i32) -> &'static str {
    if weight % 2 == 0 && weight > 2 { "YES" } else { "NO" }
}

fn main() {
    assert_eq!(watermelon(8), "YES");
    assert_eq!(watermelon(2), "NO");
    assert_eq!(watermelon(3), "NO");
    println!("4A watermelon ok");
}
