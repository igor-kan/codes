//! Horner's method for polynomial evaluation.
fn horner_with_derivative(coefficients: &[f64], x: f64) -> (f64, f64) {
    let mut value = 0.0;
    let mut derivative = 0.0;
    for &coefficient in coefficients.iter().rev() {
        derivative = derivative * x + value;
        value = value * x + coefficient;
    }
    (value, derivative)
}

fn main() {
    let coefficients = [-1.0, 2.0, -6.0, 2.0];
    let (value, derivative) = horner_with_derivative(&coefficients, 3.0);
    assert!((value - 5.0).abs() < 1e-9 && (derivative - 20.0).abs() < 1e-9);
    println!("horner ok");
}
