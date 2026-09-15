//! Classical fourth-order Runge-Kutta (Numerical Recipes 17.1).
fn rk4(f: impl Fn(f64, f64) -> f64, mut y: f64, t0: f64, t1: f64, steps: usize) -> f64 {
    let h = (t1 - t0) / steps as f64;
    let mut t = t0;
    for _ in 0..steps {
        let k1 = h * f(t, y);
        let k2 = h * f(t + h / 2.0, y + k1 / 2.0);
        let k3 = h * f(t + h / 2.0, y + k2 / 2.0);
        let k4 = h * f(t + h, y + k3);
        y += (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
        t += h;
    }
    y
}

fn main() {
    let value = rk4(|_t, y| y, 1.0, 0.0, 1.0, 1000);
    assert!((value - std::f64::consts::E).abs() < 1e-9);
    println!("runge-kutta 4 ok");
}
