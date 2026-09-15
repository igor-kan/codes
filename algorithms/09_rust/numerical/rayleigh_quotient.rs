//! Rayleigh quotient iteration.
fn rayleigh_quotient(matrix: &[Vec<f64>], vector: &[f64]) -> f64 {
    let n = matrix.len();
    let scale = vector.iter().fold(0.0f64, |acc, value| acc.max(value.abs()));
    let mut x: Vec<f64> = vector.iter().map(|value| value / scale).collect();
    let mut eigenvalue = 0.0;
    for _ in 0..100 {
        let product: Vec<f64> = (0..n)
            .map(|i| (0..n).map(|j| matrix[i][j] * x[j]).sum())
            .collect();
        let norm = product.iter().fold(0.0f64, |acc, value| acc.max(value.abs()));
        x = product.iter().map(|value| value / norm).collect();
        let numerator: f64 = (0..n)
            .map(|i| x[i] * (0..n).map(|j| matrix[i][j] * x[j]).sum::<f64>())
            .sum();
        let denominator: f64 = x.iter().map(|value| value * value).sum();
        let next = numerator / denominator;
        if (next - eigenvalue).abs() < 1e-12 {
            return next;
        }
        eigenvalue = next;
    }
    eigenvalue
}

fn main() {
    let eigenvalue = rayleigh_quotient(&[vec![2.0, 1.0], vec![1.0, 2.0]], &[1.0, 0.0]);
    assert!((eigenvalue - 3.0).abs() < 1e-9);
    println!("rayleigh quotient ok");
}
