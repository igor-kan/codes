//! Composite Simpson's rule (Numerical Recipes 4.1).
fn simpson(f: impl Fn(f64) -> f64, a: f64, b: f64, mut n: usize) -> f64 {
    if n % 2 == 1 {
        n += 1;
    }
    let h = (b - a) / n as f64;
    let mut total = f(a) + f(b);
    for i in 1..n {
        total += if i % 2 == 1 { 4.0 } else { 2.0 } * f(a + i as f64 * h);
    }
    total * h / 3.0
}

fn main() {
    assert!((simpson(|x| x * x, 0.0, 1.0, 1000) - 1.0 / 3.0).abs() < 1e-12);
    println!("simpson integration ok");
}
