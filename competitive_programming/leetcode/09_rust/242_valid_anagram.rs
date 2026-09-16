fn valid_anagram(s: &str, t: &str) -> bool {
    let mut left: Vec<char> = s.chars().collect();
    let mut right: Vec<char> = t.chars().collect();
    left.sort();
    right.sort();
    left == right
}

fn main() {
    assert!(valid_anagram("anagram", "nagaram"));
    assert!(!valid_anagram("rat", "car"));
    println!("242 valid anagram ok");
}
