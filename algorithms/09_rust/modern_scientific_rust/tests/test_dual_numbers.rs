use modern_scientific_rust::dual_numbers::Dual;

#[test]
fn test_autodiff() {
    // f(x) = x * sin(x), f'(x) = sin(x) + x * cos(x)
    let x0 = 1.5;
    let x = Dual::variable(x0);
    let f = x.mul(x.sin());

    let exact_val = x0 * x0.sin();
    let exact_der = x0.sin() + x0 * x0.cos();

    assert!((f.val - exact_val).abs() < 1e-12);
    assert!((f.der - exact_der).abs() < 1e-12);
}
