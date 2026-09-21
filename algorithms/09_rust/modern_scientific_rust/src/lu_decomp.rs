//! LU Decomposition with Partial Pivoting.

pub fn lu_factor(a: &mut [f64], n: usize) -> Option<Vec<usize>> {
    let mut piv: Vec<usize> = (0..n).collect();

    for k in 0..n - 1 {
        let mut max_idx = k;
        let mut max_val = a[k * n + k].abs();

        for i in k + 1..n {
            let val = a[i * n + k].abs();
            if val > max_val {
                max_val = val;
                max_idx = i;
            }
        }

        if max_val < 1e-15 {
            return None;
        }

        if max_idx != k {
            piv.swap(k, max_idx);
            for j in 0..n {
                a.swap(k * n + j, max_idx * n + j);
            }
        }

        for i in k + 1..n {
            a[i * n + k] /= a[k * n + k];
            for j in k + 1..n {
                a[i * n + j] -= a[i * n + k] * a[k * n + j];
            }
        }
    }

    Some(piv)
}

pub fn lu_solve(a: &[f64], piv: &[usize], b: &[f64], n: usize) -> Vec<f64> {
    let mut y = vec![0.0; n];
    for i in 0..n {
        y[i] = b[piv[i]];
        for j in 0..i {
            y[i] -= a[i * n + j] * y[j];
        }
    }

    let mut x = vec![0.0; n];
    for i in (0..n).rev() {
        x[i] = y[i];
        for j in i + 1..n {
            x[i] -= a[i * n + j] * x[j];
        }
        x[i] /= a[i * n + i];
    }
    x
}
