//! Midpoint method for ODEs.
fn midpoint_method(f: impl Fn(f64, f64) -> f64, y0: f64, t0: f64, t1: f64, steps: usize) -> f64 {
    let h = (t1 - t0) / steps as f64;
    let mut y = y0;
    let mut t = t0;
    for _ in 0..steps {
        let k1 = f(t, y);
        let k2 = f(t + h / 2.0, y + h * k1 / 2.0);
        y += h * k2;
        t += h;
    }
    y
}

fn main() {
    let value = midpoint_method(|_t, y| y, 1.0, 0.0, 1.0, 1000);
    assert!((value - std::f64::consts::E).abs() < 1e-4);
    println!("midpoint method ok");
}
