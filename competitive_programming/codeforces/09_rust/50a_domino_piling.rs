fn domino_piling(m: i64, n: i64) -> i64 {
    m * n / 2
}

fn main() {
    assert_eq!(domino_piling(2, 4), 4);
    assert_eq!(domino_piling(3, 3), 4);
    println!("50A domino piling ok");
}
