fn fizz_buzz(n: i32) -> Vec<String> {
    (1..=n).map(|value| {
        if value % 15 == 0 { "FizzBuzz".to_string() }
        else if value % 3 == 0 { "Fizz".to_string() }
        else if value % 5 == 0 { "Buzz".to_string() }
        else { value.to_string() }
    }).collect()
}

fn main() {
    assert_eq!(fizz_buzz(5), vec!["1", "2", "Fizz", "4", "Buzz"]);
    assert_eq!(fizz_buzz(15)[14], "FizzBuzz");
    println!("412 fizz buzz ok");
}
