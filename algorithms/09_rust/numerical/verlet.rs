//! Velocity Verlet integration.
fn verlet(acceleration: impl Fn(f64) -> f64, x0: f64, v0: f64, dt: f64, steps: usize) -> (f64, f64) {
    let mut x = x0;
    let mut v = v0;
    for _ in 0..steps {
        let a = acceleration(x);
        let x_new = x + v * dt + 0.5 * a * dt * dt;
        let a_new = acceleration(x_new);
        v += 0.5 * (a + a_new) * dt;
        x = x_new;
    }
    (x, v)
}

fn main() {
    let (position, velocity) = verlet(|x| -x, 1.0, 0.0, 0.001, 10000);
    let energy = 0.5 * (velocity * velocity + position * position);
    assert!((energy - 0.5).abs() < 1e-3);
    assert!((position - 10.0f64.cos()).abs() < 1e-2);
    println!("verlet ok");
}
