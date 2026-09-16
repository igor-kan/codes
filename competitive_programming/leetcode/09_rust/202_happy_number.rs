use std::collections::HashSet;

fn happy_number(n: i32) -> bool {
    let mut seen = HashSet::new();
    let mut value = n;
    while value != 1 && !seen.contains(&value) {
        seen.insert(value);
        value = value.to_string().chars().map(|d| d.to_digit(10).unwrap() as i32).map(|d| d * d).sum();
    }
    value == 1
}

fn main() {
    assert!(happy_number(19));
    assert!(!happy_number(2));
    println!("202 happy number ok");
}
