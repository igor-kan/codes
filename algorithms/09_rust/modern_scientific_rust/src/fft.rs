//! Radix-2 Cooley-Tukey Complex Fast Fourier Transform.

#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Complex {
    pub re: f64,
    pub im: f64,
}

impl Complex {
    pub fn new(re: f64, im: f64) -> Self {
        Complex { re, im }
    }

    pub fn add(self, other: Self) -> Self {
        Complex::new(self.re + other.re, self.im + other.im)
    }

    pub fn sub(self, other: Self) -> Self {
        Complex::new(self.re - other.re, self.im - other.im)
    }

    pub fn mul(self, other: Self) -> Self {
        Complex::new(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )
    }

    pub fn norm(self) -> f64 {
        (self.re * self.re + self.im * self.im).sqrt()
    }
}

pub fn fft_radix2(buf: &mut [Complex], inverse: bool) {
    let n = buf.len();
    assert!(n.is_power_of_two(), "FFT length must be power of two");

    // Bit-reversal permutation
    let mut j = 0;
    for i in 0..n {
        if i < j {
            buf.swap(i, j);
        }
        let mut bit = n >> 1;
        while j & bit != 0 {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
    }

    let pi = std::f64::consts::PI;
    let sign = if inverse { 1.0 } else { -1.0 };

    let mut len = 2;
    while len <= n {
        let angle = sign * 2.0 * pi / (len as f64);
        let w_unit = Complex::new(angle.cos(), angle.sin());

        let mut i = 0;
        while i < n {
            let mut w = Complex::new(1.0, 0.0);
            for k in 0..(len / 2) {
                let u = buf[i + k];
                let v = w.mul(buf[i + k + len / 2]);
                buf[i + k] = u.add(v);
                buf[i + k + len / 2] = u.sub(v);
                w = w.mul(w_unit);
            }
            i += len;
        }
        len <<= 1;
    }

    if inverse {
        let inv_n = 1.0 / (n as f64);
        for c in buf.iter_mut() {
            c.re *= inv_n;
            c.im *= inv_n;
        }
    }
}
