#[allow(dead_code)]
fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        let t = b;
        b = a % b;
        a = t;
    }
    a
}

fn mod_mul(a: u64, b: u64, m: u64) -> u64 {
    ((a as u128 * b as u128) % m as u128) as u64
}

fn mod_pow(mut base: u64, mut exp: u64, m: u64) -> u64 {
    let mut res = 1;
    base %= m;
    while exp > 0 {
        if exp & 1 == 1 {
            res = mod_mul(res, base, m);
        }
        base = mod_mul(base, base, m);
        exp >>= 1;
    }
    res
}

pub fn is_prime(n: u64) -> bool {
    if n < 2 { return false; }
    if n == 2 || n == 3 { return true; }
    if n % 2 == 0 { return false; }

    let mut d = n - 1;
    let mut s = 0;
    while d % 2 == 0 {
        d /= 2;
        s += 1;
    }

    let bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022];
    for &a in &bases {
        if a % n == 0 { continue; }
        let mut x = mod_pow(a, d, n);
        if x == 1 || x == n - 1 { continue; }

        let mut composite = true;
        for _ in 1..s {
            x = mod_mul(x, x, n);
            if x == n - 1 {
                composite = false;
                break;
            }
        }
        if composite { return false; }
    }
    true
}

fn main() {
    assert!(is_prime(1000000007));
    assert!(is_prime(2147483647));
    assert!(!is_prime(1000000005));
    println!("[Rust Miller-Rabin] Primality verified.");
}
