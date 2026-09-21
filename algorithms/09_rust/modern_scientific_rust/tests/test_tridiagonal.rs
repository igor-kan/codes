use modern_scientific_rust::tridiagonal::solve_tridiagonal;

#[test]
fn test_thomas_solver() {
    let a = vec![0.0, -1.0, -1.0];
    let b = vec![2.0, 2.0, 2.0];
    let c = vec![-1.0, -1.0, 0.0];
    let d = vec![1.0, 0.0, 1.0];

    let x = solve_tridiagonal(&a, &b, &c, &d).unwrap();
    assert!((x[0] - 1.0).abs() < 1e-10);
    assert!((x[1] - 1.0).abs() < 1e-10);
    assert!((x[2] - 1.0).abs() < 1e-10);
}
