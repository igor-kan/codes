//! Catalan numbers by the recurrence.
fn main() {
    let mut c = [0i64; 11];
    c[0] = 1;
    for i in 1..=10 {
        let mut sum = 0i64;
        for j in 0..i {
            sum += c[j] * c[i - 1 - j];
        }
        c[i] = sum;
    }
    assert_eq!(c[5], 42);
    assert_eq!(c[10], 16796);
    println!("catalan(10)={}", c[10]);
}
