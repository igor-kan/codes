//! Newton-Raphson root finding (Numerical Recipes 9.4).
fn newton(
    f: impl Fn(f64) -> f64,
    df: impl Fn(f64) -> f64,
    mut x: f64,
) -> f64 {
    for _ in 0..100 {
        let fx = f(x);
        if fx.abs() < 1e-12 {
            break;
        }
        x -= fx / df(x);
    }
    x
}

fn main() {
    let root = newton(|x| x * x - 2.0, |x| 2.0 * x, 1.0);
    assert!((root - 2f64.sqrt()).abs() < 1e-9);
    println!("newton-raphson ok");
}
