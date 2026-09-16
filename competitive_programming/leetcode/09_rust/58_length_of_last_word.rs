fn length_of_last_word(text: &str) -> i32 {
    text.split_whitespace().last().map(|word| word.len() as i32).unwrap_or(0)
}

fn main() {
    assert_eq!(length_of_last_word("Hello World"), 5);
    assert_eq!(length_of_last_word("   fly me   to   the moon  "), 4);
    println!("58 length of last word ok");
}
