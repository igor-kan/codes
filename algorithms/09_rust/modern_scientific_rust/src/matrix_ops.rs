//! Matrix Multiplication, Transposition, Norms.

pub fn mat_mul(a: &[f64], b: &[f64], m: usize, k: usize, n: usize) -> Vec<f64> {
    let mut c = vec![0.0; m * n];
    for i in 0..m {
        for p in 0..k {
            let a_ip = a[i * k + p];
            for j in 0..n {
                c[i * n + j] += a_ip * b[p * n + j];
            }
        }
    }
    c
}

pub fn mat_transpose(a: &[f64], rows: usize, cols: usize) -> Vec<f64> {
    let mut at = vec![0.0; rows * cols];
    for i in 0..rows {
        for j in 0..cols {
            at[j * rows + i] = a[i * cols + j];
        }
    }
    at
}

pub fn frobenius_norm(a: &[f64]) -> f64 {
    a.iter().map(|x| x * x).sum::<f64>().sqrt()
}

pub fn trace(a: &[f64], n: usize) -> f64 {
    (0..n).map(|i| a[i * n + i]).sum()
}
