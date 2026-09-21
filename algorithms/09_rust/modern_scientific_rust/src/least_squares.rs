//! Linear Least-Squares Regression.

pub fn linear_least_squares(x: &[f64], y: &[f64]) -> (f64, f64, f64) {
    let n = x.len() as f64;
    let sx: f64 = x.iter().sum();
    let sy: f64 = y.iter().sum();
    let sxx: f64 = x.iter().map(|v| v * v).sum();
    let sxy: f64 = x.iter().zip(y.iter()).map(|(a, b)| a * b).sum();

    let slope = (n * sxy - sx * sy) / (n * sxx - sx * sx);
    let intercept = (sy - slope * sx) / n;

    let y_mean = sy / n;
    let ss_tot: f64 = y.iter().map(|v| (v - y_mean).powi(2)).sum();
    let ss_res: f64 = x.iter().zip(y.iter()).map(|(a, b)| (b - (slope * a + intercept)).powi(2)).sum();
    let r_squared = 1.0 - ss_res / ss_tot;

    (slope, intercept, r_squared)
}
