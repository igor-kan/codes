//! Binomial coefficients nCr mod p in Rust.

const MOD: i64 = 1_000_000_007;

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

pub struct Factorials {
    fact: Vec<i64>,
    inv_fact: Vec<i64>,
}

impl Factorials {
    pub fn new(n: usize) -> Self {
        let mut fact = vec![1i64; n + 1];
        for i in 1..=n {
            fact[i] = fact[i - 1] * i as i64 % MOD;
        }
        let mut inv_fact = vec![1i64; n + 1];
        inv_fact[n] = mod_pow(fact[n], MOD - 2, MOD);
        for i in (0..n).rev() {
            inv_fact[i] = inv_fact[i + 1] * (i + 1) as i64 % MOD;
        }
        Factorials { fact, inv_fact }
    }

    pub fn ncr(&self, n: usize, r: usize) -> i64 {
        if r > n {
            return 0;
        }
        self.fact[n] * self.inv_fact[r] % MOD * self.inv_fact[n - r] % MOD
    }
}

fn main() {
    let f = Factorials::new(100);
    assert_eq!(f.ncr(5, 2), 10);
    assert_eq!(f.ncr(10, 3), 120);
    assert_eq!(f.ncr(10, 10), 1);
    println!("[Rust nCr] Binomial coefficients mod p verified.");
}
