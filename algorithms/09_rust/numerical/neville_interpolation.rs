//! Neville's algorithm for polynomial interpolation.
fn neville_interpolation(xs: &[f64], ys: &[f64], x: f64) -> f64 {
    let n = xs.len();
    let mut table = ys.to_vec();
    for k in 1..n {
        for i in 0..(n - k) {
            table[i] = ((x - xs[i + k]) * table[i] + (xs[i] - x) * table[i + 1]) / (xs[i] - xs[i + k]);
        }
    }
    table[0]
}

fn main() {
    let value = neville_interpolation(&[0.0, 1.0, 2.0], &[1.0, 3.0, 2.0], 1.5);
    assert!((value - 2.875).abs() < 1e-12);
    println!("neville interpolation ok");
}
