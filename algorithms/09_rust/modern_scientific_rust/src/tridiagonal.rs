//! Thomas Tridiagonal Linear System Solver O(N).

pub fn solve_tridiagonal(a: &[f64], b: &[f64], c: &[f64], d: &[f64]) -> Option<Vec<f64>> {
    let n = b.len();
    if a.len() != n || c.len() != n || d.len() != n {
        return None;
    }

    let mut c_prime = vec![0.0; n];
    let mut d_prime = vec![0.0; n];
    let mut x = vec![0.0; n];

    if b[0].abs() < 1e-15 {
        return None;
    }
    c_prime[0] = c[0] / b[0];
    d_prime[0] = d[0] / b[0];

    for i in 1..n {
        let denom = b[i] - a[i] * c_prime[i - 1];
        if denom.abs() < 1e-15 {
            return None;
        }
        c_prime[i] = c[i] / denom;
        d_prime[i] = (d[i] - a[i] * d_prime[i - 1]) / denom;
    }

    x[n - 1] = d_prime[n - 1];
    for i in (0..n - 1).rev() {
        x[i] = d_prime[i] - c_prime[i] * x[i + 1];
    }

    Some(x)
}
