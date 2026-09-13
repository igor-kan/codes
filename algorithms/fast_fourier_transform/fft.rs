use std::f64::consts::PI;

#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Complex64 {
    pub re: f64,
    pub im: f64,
}

impl Complex64 {
    pub fn new(re: f64, im: f64) -> Self {
        Complex64 { re, im }
    }

    pub fn from_polar(r: f64, theta: f64) -> Self {
        Complex64 {
            re: r * theta.cos(),
            im: r * theta.sin(),
        }
    }

    pub fn add(self, other: Self) -> Self {
        Complex64 {
            re: self.re + other.re,
            im: self.im + other.im,
        }
    }

    pub fn sub(self, other: Self) -> Self {
        Complex64 {
            re: self.re - other.re,
            im: self.im - other.im,
        }
    }

    pub fn mul(self, other: Self) -> Self {
        Complex64 {
            re: self.re * other.re - self.im * other.im,
            im: self.re * other.im + self.im * other.re,
        }
    }

    pub fn scale(self, factor: f64) -> Self {
        Complex64 {
            re: self.re * factor,
            im: self.im * factor,
        }
    }
}

pub fn bit_reverse_permute(buf: &mut [Complex64]) {
    let n = buf.len();
    let mut j = 0;
    for i in 1..n {
        let mut bit = n >> 1;
        while j & bit != 0 {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
        if i < j {
            buf.swap(i, j);
        }
    }
}

pub fn fft(buf: &mut [Complex64], invert: bool) {
    let n = buf.len();
    assert!(n.is_power_of_two());

    bit_reverse_permute(buf);

    let mut len = 2;
    while len <= n {
        let sign = if invert { -1.0 } else { 1.0 };
        let angle = 2.0 * PI / (len as f64) * sign;
        let wlen = Complex64::from_polar(1.0, angle);

        let mut i = 0;
        while i < n {
            let mut w = Complex64::new(1.0, 0.0);
            for j in 0..(len / 2) {
                let u = buf[i + j];
                let v = buf[i + j + len / 2].mul(w);
                buf[i + j] = u.add(v);
                buf[i + j + len / 2] = u.sub(v);
                w = w.mul(wlen);
            }
            i += len;
        }
        len <<= 1;
    }

    if invert {
        let inv_n = 1.0 / (n as f64);
        for x in buf.iter_mut() {
            *x = x.scale(inv_n);
        }
    }
}

fn main() {
    let mut data = vec![
        Complex64::new(1.0, 0.0),
        Complex64::new(1.0, 0.0),
        Complex64::new(1.0, 0.0),
        Complex64::new(1.0, 0.0),
        Complex64::new(0.0, 0.0),
        Complex64::new(0.0, 0.0),
        Complex64::new(0.0, 0.0),
        Complex64::new(0.0, 0.0),
    ];
    let original = data.clone();

    fft(&mut data, false);
    fft(&mut data, true);

    for (a, b) in data.iter().zip(original.iter()) {
        assert!((a.re - b.re).abs() < 1e-10);
        assert!((a.im - b.im).abs() < 1e-10);
    }
    println!("[Rust FFT] In-place zero-allocation transform verified.");
}
