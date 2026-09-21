use modern_scientific_rust::matrix_ops::{mat_mul, mat_transpose, frobenius_norm, trace};

#[test]
fn test_matrix_multiplication() {
    let a = vec![1.0, 2.0, 3.0, 4.0];
    let b = vec![2.0, 0.0, 1.0, 2.0];
    // [1 2; 3 4] * [2 0; 1 2] = [4 4; 10 8]
    let c = mat_mul(&a, &b, 2, 2, 2);
    assert_eq!(c, vec![4.0, 4.0, 10.0, 8.0]);

    let at = mat_transpose(&a, 2, 2);
    assert_eq!(at, vec![1.0, 3.0, 2.0, 4.0]);

    assert!((frobenius_norm(&a) - (30.0f64).sqrt()).abs() < 1e-12);
    assert_eq!(trace(&a, 2), 5.0);
}
