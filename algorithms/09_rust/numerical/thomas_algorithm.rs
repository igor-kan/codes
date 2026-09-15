//! Thomas algorithm for tridiagonal systems.
fn thomas_algorithm(lower: &[f64], diagonal: &[f64], upper: &[f64], rhs: &[f64]) -> Vec<f64> {
    let n = diagonal.len();
    let mut c = vec![0.0; n];
    let mut d = vec![0.0; n];
    c[0] = upper[0] / diagonal[0];
    d[0] = rhs[0] / diagonal[0];
    for i in 1..n {
        let denominator = diagonal[i] - lower[i] * c[i - 1];
        c[i] = if i < n - 1 { upper[i] / denominator } else { 0.0 };
        d[i] = (rhs[i] - lower[i] * d[i - 1]) / denominator;
    }
    let mut x = vec![0.0; n];
    x[n - 1] = d[n - 1];
    for i in (0..n - 1).rev() {
        x[i] = d[i] - c[i] * x[i + 1];
    }
    x
}

fn main() {
    let x = thomas_algorithm(&[0.0, -1.0, -1.0], &[2.0, 2.0, 2.0], &[-1.0, -1.0, 0.0], &[1.0, 0.0, 1.0]);
    assert!(x.iter().all(|value| (value - 1.0).abs() < 1e-12));
    println!("thomas algorithm ok");
}
