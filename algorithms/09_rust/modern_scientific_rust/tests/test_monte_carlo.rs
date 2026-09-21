use modern_scientific_rust::monte_carlo::monte_carlo_pi;

#[test]
fn test_mc_pi() {
    let (pi_est, std_err) = monte_carlo_pi(100_000, 42);
    let pi_true = std::f64::consts::PI;
    assert!((pi_est - pi_true).abs() < 3.0 * std_err + 0.05);
}
