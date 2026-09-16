fn palindrome_number(x: i32) -> bool {
    if x < 0 { return false; }
    let digits: Vec<char> = x.to_string().chars().collect();
    digits.iter().eq(digits.iter().rev())
}

fn main() {
    assert!(palindrome_number(121));
    assert!(!palindrome_number(-121));
    assert!(!palindrome_number(10));
    println!("9 palindrome number ok");
}
