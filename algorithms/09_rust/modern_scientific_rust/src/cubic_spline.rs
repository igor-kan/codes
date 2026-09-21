//! Natural Cubic Spline Interpolation.

pub struct Spline {
    x: Vec<f64>,
    y: Vec<f64>,
    y2: Vec<f64>,
}

impl Spline {
    pub fn new(x: Vec<f64>, y: Vec<f64>) -> Self {
        let n = x.len();
        let mut u = vec![0.0; n];
        let mut y2 = vec![0.0; n];

        for i in 1..n - 1 {
            let sig = (x[i] - x[i - 1]) / (x[i + 1] - x[i - 1]);
            let p = sig * y2[i - 1] + 2.0;
            y2[i] = (sig - 1.0) / p;
            u[i] = (6.0 * ((y[i + 1] - y[i]) / (x[i + 1] - x[i]) - (y[i] - y[i - 1]) / (x[i] - x[i - 1]))
                / (x[i + 1] - x[i - 1])
                - sig * u[i - 1])
                / p;
        }

        for k in (0..n - 1).rev() {
            y2[k] = y2[k] * y2[k + 1] + u[k];
        }

        Spline { x, y, y2 }
    }

    pub fn eval(&self, x_val: f64) -> f64 {
        let mut klo = 0;
        let mut khi = self.x.len() - 1;

        while khi - klo > 1 {
            let k = (khi + klo) / 2;
            if self.x[k] > x_val {
                khi = k;
            } else {
                klo = k;
            }
        }

        let h = self.x[khi] - self.x[klo];
        let a = (self.x[khi] - x_val) / h;
        let b = (x_val - self.x[klo]) / h;

        a * self.y[klo]
            + b * self.y[khi]
            + ((a.powi(3) - a) * self.y2[klo] + (b.powi(3) - b) * self.y2[khi]) * (h * h) / 6.0
    }
}
