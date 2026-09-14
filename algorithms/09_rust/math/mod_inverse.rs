//! Modular inverse (extended Euclid + Fermat's little theorem) in Rust.

pub fn mod_pow(mut a: i64, mut b: i64, m: i64) -> i64 {
    a %= m;
    let mut res = 1;
    while b > 0 {
        if b & 1 == 1 {
            res = res * a % m;
        }
        a = a * a % m;
        b >>= 1;
    }
    res
}

pub fn egcd(a: i64, b: i64) -> (i64, i64) {
    if b == 0 {
        (1, 0)
    } else {
        let (x, y) = egcd(b, a % b);
        (y, x - (a / b) * y)
    }
}

pub fn mod_inverse_ext(a: i64, m: i64) -> i64 {
    let (x, _) = egcd(a, m);
    ((x % m) + m) % m
}

pub fn mod_inverse_fermat(a: i64, m: i64) -> i64 {
    mod_pow(a, m - 2, m)
}

fn main() {
    const MOD: i64 = 1_000_000_007;
    assert_eq!(mod_inverse_fermat(3, MOD), 333333336);
    assert_eq!(mod_inverse_ext(3, MOD), 333333336);
    assert_eq!(3 * mod_inverse_ext(3, MOD) % MOD, 1);
    println!("[Rust ModInverse] Extended Euclid + Fermat verified.");
}
