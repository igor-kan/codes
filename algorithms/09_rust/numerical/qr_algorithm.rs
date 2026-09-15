//! QR algorithm for eigenvalues.
fn qr_decomposition(matrix: &[Vec<f64>]) -> (Vec<Vec<f64>>, Vec<Vec<f64>>) {
    let n = matrix.len();
    let mut q = vec![vec![0.0; n]; n];
    let mut r = vec![vec![0.0; n]; n];
    for j in 0..n {
        let mut v: Vec<f64> = (0..n).map(|i| matrix[i][j]).collect();
        for i in 0..j {
            r[i][j] = (0..n).map(|k| q[k][i] * v[k]).sum();
            for k in 0..n {
                v[k] -= r[i][j] * q[k][i];
            }
        }
        r[j][j] = v.iter().map(|value| value * value).sum::<f64>().sqrt();
        for k in 0..n {
            q[k][j] = v[k] / r[j][j];
        }
    }
    (q, r)
}

fn qr_algorithm(mut matrix: Vec<Vec<f64>>, iterations: usize) -> Vec<f64> {
    let n = matrix.len();
    for _ in 0..iterations {
        let (q, r) = qr_decomposition(&matrix);
        matrix = (0..n)
            .map(|i| (0..n).map(|j| (0..n).map(|k| r[i][k] * q[k][j]).sum()).collect())
            .collect();
    }
    let mut eigenvalues: Vec<f64> = (0..n).map(|i| matrix[i][i]).collect();
    eigenvalues.sort_by(|a, b| a.partial_cmp(b).unwrap());
    eigenvalues
}

fn main() {
    let eigenvalues = qr_algorithm(vec![vec![2.0, 1.0], vec![1.0, 2.0]], 1000);
    assert!((eigenvalues[0] - 1.0).abs() < 1e-6 && (eigenvalues[1] - 3.0).abs() < 1e-6);
    println!("qr algorithm ok");
}
