fn longest_common_prefix(strs: &[String]) -> String {
    if strs.is_empty() { return String::new(); }
    let mut prefix = strs[0].clone();
    for word in &strs[1..] {
        while !word.starts_with(&prefix) {
            prefix.pop();
            if prefix.is_empty() { return String::new(); }
        }
    }
    prefix
}

fn main() {
    let words: Vec<String> = ["flower", "flow", "flight"].iter().map(|s| s.to_string()).collect();
    assert_eq!(longest_common_prefix(&words), "fl");
    let none: Vec<String> = ["dog", "racecar", "car"].iter().map(|s| s.to_string()).collect();
    assert_eq!(longest_common_prefix(&none), "");
    println!("14 longest common prefix ok");
}
