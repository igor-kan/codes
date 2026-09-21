//! Bisection Root Finding.

pub fn bisection_root<F>(f: F, mut a: f64, mut b: f64, tol: f64, max_iter: usize) -> Option<(f64, usize)>
where
    F: Fn(f64) -> f64,
{
    let mut fa = f(a);
    let fb = f(b);
    if fa * fb > 0.0 {
        return None;
    }

    let mut iters = 0;
    for k in 1..=max_iter {
        iters = k;
        let c = 0.5 * (a + b);
        let fc = f(c);

        if fc.abs() < tol || (0.5 * (b - a)).abs() < tol {
            return Some((c, iters));
        }

        if fa * fc < 0.0 {
            b = c;
        } else {
            a = c;
            fa = fc;
        }
    }

    Some((0.5 * (a + b), iters))
}
