fn helpful_maths(expression: &str) -> String {
    let mut parts: Vec<&str> = expression.split('+').collect();
    parts.sort();
    parts.join("+")
}

fn main() {
    assert_eq!(helpful_maths("3+2+1"), "1+2+3");
    assert_eq!(helpful_maths("1+1+3+1+3"), "1+1+1+3+3");
    println!("339A helpful maths ok");
}
