//! Natural cubic spline interpolation.
struct Spline {
    b: Vec<f64>,
    c: Vec<f64>,
    d: Vec<f64>,
}

fn natural_cubic_spline(xs: &[f64], ys: &[f64]) -> Spline {
    let n = xs.len();
    let h: Vec<f64> = (0..n - 1).map(|i| xs[i + 1] - xs[i]).collect();
    let mut alpha = vec![0.0; n];
    for i in 1..n - 1 {
        alpha[i] = 3.0 / h[i] * (ys[i + 1] - ys[i]) - 3.0 / h[i - 1] * (ys[i] - ys[i - 1]);
    }
    let mut l = vec![0.0; n];
    let mut mu = vec![0.0; n];
    let mut z = vec![0.0; n];
    l[0] = 1.0;
    for i in 1..n - 1 {
        l[i] = 2.0 * (xs[i + 1] - xs[i - 1]) - h[i - 1] * mu[i - 1];
        mu[i] = h[i] / l[i];
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i];
    }
    let mut b = vec![0.0; n - 1];
    let mut c = vec![0.0; n];
    let mut d = vec![0.0; n - 1];
    for j in (0..n - 1).rev() {
        c[j] = z[j] - mu[j] * c[j + 1];
        b[j] = (ys[j + 1] - ys[j]) / h[j] - h[j] * (c[j + 1] + 2.0 * c[j]) / 3.0;
        d[j] = (c[j + 1] - c[j]) / (3.0 * h[j]);
    }
    Spline { b, c, d }
}

fn evaluate(xs: &[f64], ys: &[f64], spline: &Spline, x: f64) -> f64 {
    let n = xs.len();
    let mut segment = n - 2;
    for i in 0..n - 1 {
        if xs[i] <= x && x <= xs[i + 1] {
            segment = i;
            break;
        }
    }
    let dx = x - xs[segment];
    ys[segment] + spline.b[segment] * dx + spline.c[segment] * dx * dx + spline.d[segment] * dx * dx * dx
}

fn main() {
    let xs = [0.0, 1.0, 2.0, 3.0];
    let ys = [0.0, 1.0, 0.0, 1.0];
    let spline = natural_cubic_spline(&xs, &ys);
    for i in 0..xs.len() {
        assert!((evaluate(&xs, &ys, &spline, xs[i]) - ys[i]).abs() < 1e-9);
    }
    println!("cubic spline ok");
}
