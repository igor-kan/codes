//! Conjugate Gradient Method for Linear Systems (Numerical Recipes 3rd Ed. Chapter 2.7)

fn dot(a: &[f64], b: &[f64]) -> f64 {
    a.iter().zip(b).map(|(x, y)| x * y).sum()
}

fn mat_vec(a: &[Vec<f64>], v: &[f64]) -> Vec<f64> {
    a.iter().map(|row| dot(row, v)).collect()
}

pub fn conjugate_gradient(a: &[Vec<f64>], b: &[f64], tol: f64, max_iter: usize) -> Vec<f64> {
    let n = b.len();
    let mut x = vec![0.0; n];
    let mut r = b.to_vec();
    let mut p = r.clone();
    let mut rs_old = dot(&r, &r);

    for _ in 0..max_iter {
        if rs_old.sqrt() < tol {
            break;
        }
        let ap = mat_vec(a, &p);
        let alpha = rs_old / dot(&p, &ap);

        for i in 0..n {
            x[i] += alpha * p[i];
            r[i] -= alpha * ap[i];
        }

        let rs_new = dot(&r, &r);
        for i in 0..n {
            p[i] = r[i] + (rs_new / rs_old) * p[i];
        }
        rs_old = rs_new;
    }
    x
}

fn main() {
    let a = vec![vec![4.0, 1.0], vec![1.0, 3.0]];
    let b = vec![1.0, 2.0];
    let x = conjugate_gradient(&a, &b, 1e-8, 50);
    assert!((x[0] - 1.0 / 11.0).abs() < 1e-5);
    println!("Rust Conjugate Gradient verified.");
}
