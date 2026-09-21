use modern_scientific_rust::cubic_spline::Spline;

#[test]
fn test_spline_interpolation() {
    let x = vec![0.0, 1.0, 2.0, 3.0, 4.0];
    let y = vec![0.0, 1.0, 4.0, 9.0, 16.0];
    let sp = Spline::new(x, y);

    let val = sp.eval(2.5);
    // Exact y(2.5) = 6.25
    assert!((val - 6.25).abs() < 0.2);
}
