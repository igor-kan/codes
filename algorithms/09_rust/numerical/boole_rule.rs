//! Composite Boole's rule.
fn boole_rule(f: impl Fn(f64) -> f64, a: f64, b: f64, mut n: usize) -> f64 {
    if n % 4 != 0 {
        n += 4 - n % 4;
    }
    let h = (b - a) / n as f64;
    let mut total = 7.0 * (f(a) + f(b));
    for i in 1..n {
        total += if i % 4 == 0 {
            14.0
        } else if i % 2 == 0 {
            12.0
        } else {
            32.0
        } * f(a + i as f64 * h);
    }
    2.0 * h / 45.0 * total
}

fn main() {
    assert!((boole_rule(|x| x * x, 0.0, 1.0, 998) - 1.0 / 3.0).abs() < 1e-12);
    println!("boole rule ok");
}
