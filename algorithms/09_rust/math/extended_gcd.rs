//! Extended Euclidean Algorithm (CLRS 3rd Ed. Chapter 31.2)
//! Computes gcd(a, b) and Bezout coefficients ax + by = gcd(a, b).

pub fn extended_gcd(a: i64, b: i64) -> (i64, i64, i64) {
    if b == 0 {
        (a, 1, 0)
    } else {
        let (gcd, x1, y1) = extended_gcd(b, a % b);
        let x = y1;
        let y = x1 - (a / b) * y1;
        (gcd, x, y)
    }
}

fn main() {
    let (g, x, y) = extended_gcd(240, 46);
    assert_eq!(g, 2);
    assert_eq!(240 * x + 46 * y, 2);
    println!("Rust Extended GCD verified.");
}
