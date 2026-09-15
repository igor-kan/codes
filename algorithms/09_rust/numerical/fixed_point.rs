//! Fixed-point iteration.
fn fixed_point(g: impl Fn(f64) -> f64, x: f64) -> f64 {
    let mut current = x;
    for _ in 0..200 {
        let next = g(current);
        if (next - current).abs() < 1e-12 {
            return next;
        }
        current = next;
    }
    current
}

fn main() {
    let root = fixed_point(|x| 0.5 * (x + 2.0 / x), 1.0);
    assert!((root - 2f64.sqrt()).abs() < 1e-9);
    println!("fixed point ok");
}
