//! Closest pair of points (quadratic brute force).
fn main() {
    let pts: [(f64, f64); 6] = [
        (2.0, 3.0),
        (12.0, 30.0),
        (40.0, 50.0),
        (5.0, 1.0),
        (12.0, 10.0),
        (3.0, 4.0),
    ];
    let mut best = f64::MAX;
    for i in 0..pts.len() {
        for j in i + 1..pts.len() {
            let d = ((pts[i].0 - pts[j].0).powi(2) + (pts[i].1 - pts[j].1).powi(2)).sqrt();
            if d < best {
                best = d;
            }
        }
    }
    assert!((best - (2.0_f64).sqrt()).abs() < 1e-9);
    println!("closest={}", best);
}
