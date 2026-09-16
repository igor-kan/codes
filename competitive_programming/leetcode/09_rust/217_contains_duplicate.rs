use std::collections::HashSet;

fn contains_duplicate(nums: &[i32]) -> bool {
    let mut seen = HashSet::new();
    nums.iter().any(|&value| !seen.insert(value))
}

fn main() {
    assert!(contains_duplicate(&[1, 2, 3, 1]));
    assert!(!contains_duplicate(&[1, 2, 3, 4]));
    println!("217 contains duplicate ok");
}
