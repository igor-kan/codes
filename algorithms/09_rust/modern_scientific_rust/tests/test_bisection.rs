use modern_scientific_rust::bisection::bisection_root;

#[test]
fn test_bisection() {
    // f(x) = x^2 - 2 -> root = sqrt(2)
    let (root, iters) = bisection_root(|x| x * x - 2.0, 1.0, 2.0, 1e-10, 100).unwrap();
    assert!((root - std::f64::consts::SQRT_2).abs() < 1e-9);
    assert!(iters > 0);
}
