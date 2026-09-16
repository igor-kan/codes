fn value(c: char) -> i32 {
    match c {
        'I' => 1, 'V' => 5, 'X' => 10, 'L' => 50,
        'C' => 100, 'D' => 500, _ => 1000,
    }
}

fn roman_to_integer(text: &str) -> i32 {
    let chars: Vec<char> = text.chars().collect();
    let mut total = 0;
    for i in 0..chars.len() {
        let current = value(chars[i]);
        if i + 1 < chars.len() && current < value(chars[i + 1]) { total -= current; }
        else { total += current; }
    }
    total
}

fn main() {
    assert_eq!(roman_to_integer("III"), 3);
    assert_eq!(roman_to_integer("LVIII"), 58);
    assert_eq!(roman_to_integer("MCMXCIV"), 1994);
    println!("13 roman to integer ok");
}
