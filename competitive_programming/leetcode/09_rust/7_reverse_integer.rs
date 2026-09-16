fn reverse_integer(x: i32) -> i32 {
    let sign: i64 = if x < 0 { -1 } else { 1 };
    let mut value = (x as i64).abs();
    let mut reversed: i64 = 0;
    while value > 0 { reversed = reversed * 10 + value % 10; value /= 10; }
    reversed *= sign;
    if reversed < -(1i64 << 31) || reversed > (1i64 << 31) - 1 { 0 } else { reversed as i32 }
}

fn main() {
    assert_eq!(reverse_integer(123), 321);
    assert_eq!(reverse_integer(-123), -321);
    assert_eq!(reverse_integer(120), 21);
    assert_eq!(reverse_integer(1534236469), 0);
    println!("7 reverse integer ok");
}
