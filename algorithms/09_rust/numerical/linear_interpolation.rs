//! Piecewise linear interpolation.
fn linear_interpolation(xs: &[f64], ys: &[f64], x: f64) -> f64 {
    if x <= xs[0] {
        return ys[0];
    }
    if x >= xs[xs.len() - 1] {
        return ys[ys.len() - 1];
    }
    for i in 1..xs.len() {
        if x <= xs[i] {
            let slope = (ys[i] - ys[i - 1]) / (xs[i] - xs[i - 1]);
            return ys[i - 1] + slope * (x - xs[i - 1]);
        }
    }
    ys[ys.len() - 1]
}

fn main() {
    assert!((linear_interpolation(&[0.0, 1.0, 2.0], &[0.0, 2.0, 4.0], 0.5) - 1.0).abs() < 1e-12);
    assert!((linear_interpolation(&[0.0, 1.0, 4.0], &[0.0, 1.0, 2.0], 2.5) - 1.5).abs() < 1e-12);
    println!("linear interpolation ok");
}
