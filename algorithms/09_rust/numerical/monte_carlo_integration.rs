//! Monte Carlo integration.
fn monte_carlo_integration(f: impl Fn(f64) -> f64, a: f64, b: f64, samples: usize) -> f64 {
    let modulus: i64 = 1 << 31;
    let mut state: i64 = 42;
    let mut total = 0.0;
    for _ in 0..samples {
        state = (1103515245 * state + 12345) % modulus;
        total += f(a + (b - a) * state as f64 / modulus as f64);
    }
    (b - a) * total / samples as f64
}

fn main() {
    let estimate = monte_carlo_integration(|x| x * x, 0.0, 1.0, 100000);
    assert!((estimate - 1.0 / 3.0).abs() < 0.01);
    println!("monte carlo integration ok");
}
