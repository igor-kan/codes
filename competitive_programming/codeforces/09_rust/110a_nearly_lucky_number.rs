fn nearly_lucky_number(number: i64) -> &'static str {
    let count = number.to_string().chars().filter(|&digit| digit == '4' || digit == '7').count();
    if count == 4 || count == 7 { "YES" } else { "NO" }
}

fn main() {
    assert_eq!(nearly_lucky_number(47), "NO");
    assert_eq!(nearly_lucky_number(7747774), "YES");
    assert_eq!(nearly_lucky_number(40047), "NO");
    println!("110A nearly lucky number ok");
}
