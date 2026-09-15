fn bit_plus_plus(operations: &[&str]) -> i32 {
    operations.iter().map(|operation| if operation.contains("++") { 1 } else { -1 }).sum()
}

fn main() {
    assert_eq!(bit_plus_plus(&["++X", "X++", "--X"]), 1);
    assert_eq!(bit_plus_plus(&["X++", "X++", "X++", "X--"]), 2);
    println!("282A bit++ ok");
}
