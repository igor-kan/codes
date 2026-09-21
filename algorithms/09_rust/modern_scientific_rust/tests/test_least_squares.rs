use modern_scientific_rust::least_squares::linear_least_squares;

#[test]
fn test_linear_regression() {
    let x = vec![1.0, 2.0, 3.0, 4.0, 5.0];
    let y = vec![3.0, 5.0, 7.0, 9.0, 11.0]; // y = 2x + 1
    let (m, c, r2) = linear_least_squares(&x, &y);

    assert!((m - 2.0).abs() < 1e-10);
    assert!((c - 1.0).abs() < 1e-10);
    assert!((r2 - 1.0).abs() < 1e-10);
}
