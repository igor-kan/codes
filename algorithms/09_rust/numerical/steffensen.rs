//! Steffensen's method.
fn steffensen(g: impl Fn(f64) -> f64, x: f64) -> f64 {
    let mut current = x;
    for _ in 0..100 {
        let x1 = g(current);
        let x2 = g(x1);
        let denominator = x2 - 2.0 * x1 + current;
        if denominator.abs() < 1e-15 {
            return x2;
        }
        let next = current - (x1 - current).powi(2) / denominator;
        if (next - current).abs() < 1e-12 {
            return next;
        }
        current = next;
    }
    current
}

fn main() {
    let root = steffensen(|x| 0.5 * (x + 2.0 / x), 1.0);
    assert!((root - 2f64.sqrt()).abs() < 1e-12);
    println!("steffensen ok");
}
