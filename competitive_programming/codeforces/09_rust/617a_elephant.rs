fn elephant(position: i32) -> i32 {
    (position + 4) / 5
}

fn main() {
    assert_eq!(elephant(5), 1);
    assert_eq!(elephant(12), 3);
    assert_eq!(elephant(1), 1);
    println!("617A elephant ok");
}
