//! Golden-Section 1D Unimodal Function Minimizer.

pub fn golden_section_search<F>(f: F, mut a: f64, mut b: f64, tol: f64, max_iter: usize) -> (f64, f64, usize)
where
    F: Fn(f64) -> f64,
{
    let phi_inv = 0.6180339887498948;
    let mut c = b - phi_inv * (b - a);
    let mut d = a + phi_inv * (b - a);
    let mut fc = f(c);
    let mut fd = f(d);

    let mut iters = 0;
    for k in 1..=max_iter {
        iters = k;
        if (b - a).abs() < tol {
            break;
        }

        if fc < fd {
            b = d;
            d = c;
            fd = fc;
            c = b - phi_inv * (b - a);
            fc = f(c);
        } else {
            a = c;
            c = d;
            fc = fd;
            d = a + phi_inv * (b - a);
            fd = f(d);
        }
    }

    let x_min = 0.5 * (a + b);
    (x_min, f(x_min), iters)
}
