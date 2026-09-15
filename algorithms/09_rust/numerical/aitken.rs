//! Aitken's delta-squared acceleration.
fn aitken(x0: f64, x1: f64, x2: f64) -> f64 {
    let denominator = x2 - 2.0 * x1 + x0;
    if denominator.abs() < 1e-15 {
        return x2;
    }
    x2 - (x2 - x1).powi(2) / denominator
}

fn main() {
    assert!(aitken(1.0, 0.5, 0.25).abs() < 1e-12);
    let sequence: Vec<f64> = (0..3).map(|n| 2.0 - 2.0 * 0.5f64.powi(n)).collect();
    assert!((aitken(sequence[0], sequence[1], sequence[2]) - 2.0).abs() < 1e-12);
    println!("aitken ok");
}
