use modern_scientific_rust::golden_section::golden_section_search;

#[test]
fn test_golden_search() {
    // Min of f(x) = (x - 3)^2 + 4 is at x = 3
    let (xmin, fmin, _) = golden_section_search(|x| (x - 3.0).powi(2) + 4.0, 0.0, 5.0, 1e-8, 100);
    assert!((xmin - 3.0).abs() < 1e-7);
    assert!((fmin - 4.0).abs() < 1e-7);
}
