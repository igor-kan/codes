//! Cooley-Tukey FFT in Rust (CLRS 3rd Ed. Chapter 30.2)

use std::f64::consts::PI;

#[derive(Clone, Copy, Debug)]
pub struct Complex {
    pub re: f64,
    pub im: f64,
}

impl Complex {
    pub fn new(re: f64, im: f64) -> Self {
        Complex { re, im }
    }
    pub fn add(self, o: Self) -> Self {
        Complex::new(self.re + o.re, self.im + o.im)
    }
    pub fn sub(self, o: Self) -> Self {
        Complex::new(self.re - o.re, self.im - o.im)
    }
    pub fn mul(self, o: Self) -> Self {
        Complex::new(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    }
}

pub fn fft(a: &[Complex], invert: bool) -> Vec<Complex> {
    let n = a.len();
    if n == 1 {
        return vec![a[0]];
    }

    let mut a0 = Vec::with_capacity(n / 2);
    let mut a1 = Vec::with_capacity(n / 2);
    for i in 0..n / 2 {
        a0.push(a[2 * i]);
        a1.push(a[2 * i + 1]);
    }

    let y0 = fft(&a0, invert);
    let y1 = fft(&a1, invert);

    let mut y = vec![Complex::new(0.0, 0.0); n];
    let angle = (if invert { -2.0 } else { 2.0 }) * PI / (n as f64);
    let mut w = Complex::new(1.0, 0.0);
    let wn = Complex::new(angle.cos(), angle.sin());

    for k in 0..n / 2 {
        let term = w.mul(y1[k]);
        y[k] = y0[k].add(term);
        y[k + n / 2] = y0[k].sub(term);
        if invert {
            y[k].re /= 2.0;
            y[k].im /= 2.0;
            y[k + n / 2].re /= 2.0;
            y[k + n / 2].im /= 2.0;
        }
        w = w.mul(wn);
    }
    y
}

fn main() {
    let sig = vec![Complex::new(1.0, 0.0), Complex::new(2.0, 0.0), Complex::new(3.0, 0.0), Complex::new(4.0, 0.0)];
    let res = fft(&sig, false);
    let inv = fft(&res, true);
    assert!((inv[0].re - 1.0).abs() < 1e-6);
    println!("Rust FFT verified.");
}
