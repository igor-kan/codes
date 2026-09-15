//! Regula falsi root finding.
fn regula_falsi(f: impl Fn(f64) -> f64, mut a: f64, mut b: f64) -> f64 {
    let mut fa = f(a);
    let mut fb = f(b);
    if fa * fb > 0.0 {
        panic!("root is not bracketed");
    }
    let mut c = a;
    for _ in 0..200 {
        c = (a * fb - b * fa) / (fb - fa);
        let fc = f(c);
        if fc.abs() < 1e-12 {
            return c;
        }
        if fa * fc < 0.0 {
            b = c;
            fb = fc;
        } else {
            a = c;
            fa = fc;
        }
    }
    c
}

fn main() {
    let root = regula_falsi(|x| x * x - 2.0, 0.0, 2.0);
    assert!((root - 2f64.sqrt()).abs() < 1e-9);
    println!("regula falsi ok");
}
