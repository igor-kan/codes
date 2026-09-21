//! Composite Simpson's 1/3 and Gauss-Legendre Quadrature.

pub fn simpson_quadrature<F>(f: F, a: f64, b: f64, n_intervals: usize) -> f64
where
    F: Fn(f64) -> f64,
{
    let n = if n_intervals % 2 == 0 { n_intervals } else { n_intervals + 1 };
    let h = (b - a) / (n as f64);
    let mut sum_odd = 0.0;
    let mut sum_even = 0.0;

    for i in 1..n {
        let x = a + (i as f64) * h;
        if i % 2 == 0 {
            sum_even += f(x);
        } else {
            sum_odd += f(x);
        }
    }

    (h / 3.0) * (f(a) + 4.0 * sum_odd + 2.0 * sum_even + f(b))
}

pub fn gauss_legendre_2point<F>(f: F, a: f64, b: f64) -> f64
where
    F: Fn(f64) -> f64,
{
    let inv_sqrt3 = 1.0 / (3.0f64).sqrt();
    let x1 = 0.5 * ((b - a) * (-inv_sqrt3) + (a + b));
    let x2 = 0.5 * ((b - a) * inv_sqrt3 + (a + b));
    0.5 * (b - a) * (f(x1) + f(x2))
}
