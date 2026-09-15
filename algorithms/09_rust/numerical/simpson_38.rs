//! Composite Simpson's 3/8 rule.
fn simpson_38(f: impl Fn(f64) -> f64, a: f64, b: f64, mut n: usize) -> f64 {
    if n % 3 != 0 {
        n += 3 - n % 3;
    }
    let h = (b - a) / n as f64;
    let mut total = f(a) + f(b);
    for i in 1..n {
        total += if i % 3 != 0 { 3.0 } else { 2.0 } * f(a + i as f64 * h);
    }
    3.0 * h / 8.0 * total
}

fn main() {
    assert!((simpson_38(|x| x * x, 0.0, 1.0, 999) - 1.0 / 3.0).abs() < 1e-12);
    println!("simpson 3/8 ok");
}
