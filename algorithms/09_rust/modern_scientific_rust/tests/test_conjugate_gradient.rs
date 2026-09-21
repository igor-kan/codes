use modern_scientific_rust::conjugate_gradient::conjugate_gradient;

#[test]
fn test_cg_solver() {
    let a = vec![4.0, 1.0, 1.0, 3.0];
    let b = vec![1.0, 2.0];
    let (x, iters, res) = conjugate_gradient(&a, &b, 50, 1e-10);
    // 4 x1 + x2 = 1, x1 + 3 x2 = 2 -> x1 = 1/11, x2 = 7/11
    assert!((x[0] - 1.0 / 11.0).abs() < 1e-8);
    assert!((x[1] - 7.0 / 11.0).abs() < 1e-8);
    assert!(res < 1e-10);
    assert!(iters <= 2);
}
