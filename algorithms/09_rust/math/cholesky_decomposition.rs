//! Cholesky Decomposition LL^T (Numerical Recipes 3rd Ed. Chapter 2.6)
//! Symmetric positive-definite matrix factorization.

pub fn cholesky(a: &[Vec<f64>]) -> Vec<Vec<f64>> {
    let n = a.len();
    let mut l = vec![vec![0.0; n]; n];

    for i in 0..n {
        for j in 0..=i {
            let mut sum = 0.0;
            for k in 0..j {
                sum += l[i][k] * l[j][k];
            }
            if i == j {
                let val = a[i][i] - sum;
                assert!(val > 0.0, "Matrix not positive definite");
                l[i][j] = val.sqrt();
            } else {
                l[i][j] = (a[i][j] - sum) / l[j][j];
            }
        }
    }
    l
}

fn main() {
    let a = vec![vec![4.0, 12.0, -16.0], vec![12.0, 37.0, -43.0], vec![-16.0, -43.0, 98.0]];
    let l = cholesky(&a);
    assert!((l[0][0] - 2.0).abs() < 1e-6);
    println!("Rust Cholesky Decomposition verified.");
}
