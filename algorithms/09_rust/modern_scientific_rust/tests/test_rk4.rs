use modern_scientific_rust::rk4::rk4_integrate;

#[test]
fn test_rk4_exponential_decay() {
    let (t, y) = rk4_integrate(0.0, 2.0, &[1.0], 100, |_t, y| vec![-y[0]]);
    let exact = (-2.0f64).exp();
    let final_y = y.last().unwrap()[0];
    assert!((final_y - exact).abs() < 1e-6);
    assert_eq!(t.len(), 101);
}
