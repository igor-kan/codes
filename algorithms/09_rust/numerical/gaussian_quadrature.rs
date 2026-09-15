//! Gauss-Legendre quadrature (5-point).
const NODES: [f64; 5] = [0.0, -0.5384693101056831, 0.5384693101056831, -0.9061798459386640, 0.9061798459386640];
const WEIGHTS: [f64; 5] = [0.5688888888888889, 0.4786286704993665, 0.4786286704993665, 0.2369268850561891, 0.2369268850561891];

fn gaussian_quadrature(f: impl Fn(f64) -> f64, a: f64, b: f64) -> f64 {
    let midpoint = 0.5 * (a + b);
    let half = 0.5 * (b - a);
    let mut total = 0.0;
    for i in 0..5 {
        total += WEIGHTS[i] * f(midpoint + half * NODES[i]);
    }
    total * half
}

fn main() {
    assert!((gaussian_quadrature(|x| x * x, 0.0, 1.0) - 1.0 / 3.0).abs() < 1e-12);
    assert!((gaussian_quadrature(|x| x.powi(7), 0.0, 1.0) - 1.0 / 8.0).abs() < 1e-12);
    println!("gaussian quadrature ok");
}
