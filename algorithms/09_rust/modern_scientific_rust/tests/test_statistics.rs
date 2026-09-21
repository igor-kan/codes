use modern_scientific_rust::statistics::{mean, variance, std_dev, pearson_correlation};

#[test]
fn test_stats() {
    let d = vec![2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0];
    assert_eq!(mean(&d), 5.0);
    assert!((variance(&d) - 32.0 / 7.0).abs() < 1e-12);
    assert!((std_dev(&d) - (32.0f64 / 7.0).sqrt()).abs() < 1e-12);

    let x = vec![1.0, 2.0, 3.0, 4.0, 5.0];
    let y = vec![2.0, 4.0, 6.0, 8.0, 10.0];
    assert!((pearson_correlation(&x, &y) - 1.0).abs() < 1e-12);
}
