//! Kalman Filter in Rust (Numerical Recipes 3rd Ed. Chapter 15)

pub struct KalmanFilter1D {
    pub x: f64,
    pub p: f64,
    pub q: f64,
    pub r: f64,
}

impl KalmanFilter1D {
    pub fn new(x: f64, p: f64, q: f64, r: f64) -> Self {
        KalmanFilter1D { x, p, q, r }
    }

    pub fn predict(&mut self) {
        self.p += self.q;
    }

    pub fn update(&mut self, z: f64) -> f64 {
        let k = self.p / (self.p + self.r);
        self.x += k * (z - self.x);
        self.p = (1.0 - k) * self.p;
        self.x
    }
}

fn main() {
    let mut kf = KalmanFilter1D::new(0.0, 1.0, 0.01, 0.1);
    for &z in &[0.9, 1.1, 0.95, 1.05] {
        kf.predict();
        kf.update(z);
    }
    assert!((kf.x - 1.0).abs() < 0.2);
    println!("Rust Kalman Filter verified.");
}
