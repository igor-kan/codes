use modern_scientific_rust::quadrature::{simpson_quadrature, gauss_legendre_2point};

#[test]
fn test_integration() {
    let exact = 2.0;
    let val_simp = simpson_quadrature(|x| x.sin(), 0.0, std::f64::consts::PI, 100);
    assert!((val_simp - exact).abs() < 1e-6);

    // Gauss-Legendre 2-point integrates polynomials up to degree 3 exactly: int_0^1 x^3 dx = 0.25
    let val_gauss = gauss_legendre_2point(|x| x.powi(3), 0.0, 1.0);
    assert!((val_gauss - 0.25).abs() < 1e-12);
}
