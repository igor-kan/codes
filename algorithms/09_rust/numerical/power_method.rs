//! Power iteration for the dominant eigenvalue.
fn power_method(matrix: &[Vec<f64>]) -> (f64, Vec<f64>) {
    let n = matrix.len();
    let mut vector = vec![1.0; n];
    let mut eigenvalue = 0.0;
    for _ in 0..1000 {
        let product: Vec<f64> = (0..n)
            .map(|i| (0..n).map(|j| matrix[i][j] * vector[j]).sum())
            .collect();
        let norm = product.iter().fold(0.0f64, |acc, value| acc.max(value.abs()));
        vector = product.iter().map(|value| value / norm).collect();
        if (norm - eigenvalue).abs() < 1e-12 {
            eigenvalue = norm;
            break;
        }
        eigenvalue = norm;
    }
    (eigenvalue, vector)
}

fn main() {
    let matrix = vec![vec![4.0, 1.0], vec![2.0, 3.0]];
    let (eigenvalue, vector) = power_method(&matrix);
    assert!((eigenvalue - 5.0).abs() < 1e-9);
    for i in 0..2 {
        let residual = matrix[i][0] * vector[0] + matrix[i][1] * vector[1] - eigenvalue * vector[i];
        assert!(residual.abs() < 1e-9);
    }
    println!("power method ok");
}
