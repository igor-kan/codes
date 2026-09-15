//! Ordinary least squares for a straight line.
fn least_squares_linear(xs: &[f64], ys: &[f64]) -> (f64, f64) {
    let n = xs.len() as f64;
    let mean_x: f64 = xs.iter().sum::<f64>() / n;
    let mean_y: f64 = ys.iter().sum::<f64>() / n;
    let numerator: f64 = xs.iter().zip(ys).map(|(x, y)| (x - mean_x) * (y - mean_y)).sum();
    let denominator: f64 = xs.iter().map(|x| (x - mean_x).powi(2)).sum();
    let slope = numerator / denominator;
    (mean_y - slope * mean_x, slope)
}

fn main() {
    let (intercept, slope) = least_squares_linear(&[0.0, 1.0, 2.0, 3.0], &[1.0, 3.0, 5.0, 7.0]);
    assert!((intercept - 1.0).abs() < 1e-12 && (slope - 2.0).abs() < 1e-12);
    println!("least squares linear ok");
}
