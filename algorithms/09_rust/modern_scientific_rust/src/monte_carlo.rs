//! Monte Carlo Integrator with LCG Pseudo-Random Number Generator.

struct Lcg {
    state: u64,
}

impl Lcg {
    fn new(seed: u64) -> Self {
        Lcg { state: seed }
    }

    fn next_f64(&mut self) -> f64 {
        self.state = self.state.wrapping_mul(6364136223846793005).wrapping_add(1);
        (self.state >> 11) as f64 / (1u64 << 53) as f64
    }
}

pub fn monte_carlo_pi(n_samples: usize, seed: u64) -> (f64, f64) {
    let mut rng = Lcg::new(seed);
    let mut inside = 0;

    for _ in 0..n_samples {
        let x = rng.next_f64();
        let y = rng.next_f64();
        if x * x + y * y <= 1.0 {
            inside += 1;
        }
    }

    let p = (inside as f64) / (n_samples as f64);
    let pi_est = 4.0 * p;
    let std_err = 4.0 * (p * (1.0 - p) / (n_samples as f64)).sqrt();
    (pi_est, std_err)
}
