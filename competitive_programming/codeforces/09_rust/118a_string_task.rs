fn string_task(text: &str) -> String {
    let vowels = "aeiouy";
    let mut result = String::new();
    for character in text.to_lowercase().chars() {
        if !vowels.contains(character) {
            result.push('.');
            result.push(character);
        }
    }
    result
}

fn main() {
    assert_eq!(string_task("Codeforces"), ".c.d.f.r.c.s");
    assert_eq!(string_task("aBAcAba"), ".b.c.b");
    println!("118A string task ok");
}
