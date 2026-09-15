//! Bisection root finding.
fn bisection(f: impl Fn(f64) -> f64, mut a: f64, mut b: f64) -> f64 {
    let mut fa = f(a);
    let fb = f(b);
    if fa * fb > 0.0 {
        panic!("root is not bracketed");
    }
    let mut c = a;
    for _ in 0..200 {
        c = 0.5 * (a + b);
        let fc = f(c);
        if fc == 0.0 || (b - a) / 2.0 < 1e-12 {
            return c;
        }
        if fa * fc < 0.0 {
            b = c;
        } else {
            a = c;
            fa = fc;
        }
    }
    c
}

fn main() {
    let root = bisection(|x| x * x - 2.0, 0.0, 2.0);
    assert!((root - 2f64.sqrt()).abs() < 1e-9);
    println!("bisection ok");
}
