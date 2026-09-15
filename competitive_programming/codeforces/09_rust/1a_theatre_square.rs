fn theatre_square(n: i64, m: i64, a: i64) -> i64 {
    ((n + a - 1) / a) * ((m + a - 1) / a)
}

fn main() {
    assert_eq!(theatre_square(6, 6, 4), 4);
    assert_eq!(theatre_square(1, 1, 1), 1);
    println!("1A theatre square ok");
}
