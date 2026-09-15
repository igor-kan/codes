//! Forward Euler method for ODEs.
fn euler_method(f: impl Fn(f64, f64) -> f64, y0: f64, t0: f64, t1: f64, steps: usize) -> f64 {
    let h = (t1 - t0) / steps as f64;
    let mut y = y0;
    let mut t = t0;
    for _ in 0..steps {
        y += h * f(t, y);
        t += h;
    }
    y
}

fn main() {
    let value = euler_method(|_t, y| y, 1.0, 0.0, 1.0, 1000);
    assert!((value - std::f64::consts::E).abs() < 0.01);
    println!("euler method ok");
}
