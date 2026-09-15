fn way_too_long(word: &str) -> String {
    let chars: Vec<char> = word.chars().collect();
    if chars.len() <= 10 {
        word.to_string()
    } else {
        format!("{}{}{}", chars[0], chars.len() - 2, chars[chars.len() - 1])
    }
}

fn main() {
    assert_eq!(way_too_long("word"), "word");
    assert_eq!(way_too_long("localization"), "l10n");
    assert_eq!(way_too_long("internationalization"), "i18n");
    println!("71A way too long words ok");
}
