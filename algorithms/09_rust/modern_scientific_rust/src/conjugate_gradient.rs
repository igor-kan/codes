//! Iterative Conjugate Gradient Linear Solver.

pub fn conjugate_gradient(a: &[f64], b: &[f64], max_iter: usize, tol: f64) -> (Vec<f64>, usize, f64) {
    let n = b.len();
    let mut x = vec![0.0; n];
    let mut r = b.to_vec();
    let mut p = r.clone();

    let mut rs_old = dot(&r, &r);
    if rs_old.sqrt() < tol {
        return (x, 0, rs_old.sqrt());
    }

    let mut iters = 0;
    for k in 0..max_iter {
        iters = k + 1;
        let ap = mat_vec(a, &p, n);
        let alpha = rs_old / dot(&p, &ap);

        for i in 0..n {
            x[i] += alpha * p[i];
            r[i] -= alpha * ap[i];
        }

        let rs_new = dot(&r, &r);
        if rs_new.sqrt() < tol {
            return (x, iters, rs_new.sqrt());
        }

        let beta = rs_new / rs_old;
        for i in 0..n {
            p[i] = r[i] + beta * p[i];
        }
        rs_old = rs_new;
    }

    (x, iters, rs_old.sqrt())
}

fn dot(u: &[f64], v: &[f64]) -> f64 {
    u.iter().zip(v.iter()).map(|(a, b)| a * b).sum()
}

fn mat_vec(a: &[f64], x: &[f64], n: usize) -> Vec<f64> {
    let mut y = vec![0.0; n];
    for i in 0..n {
        for j in 0..n {
            y[i] += a[i * n + j] * x[j];
        }
    }
    y
}
