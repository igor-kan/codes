//! Dual Numbers Forward-Mode Automatic Differentiation.

#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Dual {
    pub val: f64,
    pub der: f64,
}

impl Dual {
    pub fn constant(val: f64) -> Self {
        Dual { val, der: 0.0 }
    }

    pub fn variable(val: f64) -> Self {
        Dual { val, der: 1.0 }
    }

    pub fn add(self, other: Self) -> Self {
        Dual { val: self.val + other.val, der: self.der + other.der }
    }

    pub fn mul(self, other: Self) -> Self {
        Dual {
            val: self.val * other.val,
            der: self.val * other.der + self.der * other.val,
        }
    }

    pub fn sin(self) -> Self {
        Dual { val: self.val.sin(), der: self.der * self.val.cos() }
    }

    pub fn cos(self) -> Self {
        Dual { val: self.val.cos(), der: -self.der * self.val.sin() }
    }

    pub fn exp(self) -> Self {
        let e = self.val.exp();
        Dual { val: e, der: self.der * e }
    }
}
