//! Brent's Method for Root Finding (Numerical Recipes 3rd Ed. Chapter 9.3)
//! Guaranteed convergence combining Bisection, Secant, and Inverse Quadratic Interpolation.

pub fn brent_root<F: Fn(f64) -> f64>(f: F, mut a: f64, mut b: f64, tol: f64, max_iter: usize) -> f64 {
    let mut fa = f(a);
    let mut fb = f(b);
    assert!(fa * fb <= 0.0, "Root not bracketed");

    if fa.abs() < fb.abs() {
        std::mem::swap(&mut a, &mut b);
        std::mem::swap(&mut fa, &mut fb);
    }

    let mut c = a;
    let mut fc = fa;
    let mut mflag = true;
    let mut s = b;
    let mut d = 0.0;

    for _ in 0..max_iter {
        if fb.abs() < tol || (b - a).abs() < tol {
            return b;
        }

        if fa != fc && fb != fc {
            s = (a * fb * fc) / ((fa - fb) * (fa - fc))
                + (b * fa * fc) / ((fb - fa) * (fb - fc))
                + (c * fa * fb) / ((fc - fa) * (fc - fb));
        } else {
            s = b - fb * ((b - a) / (fb - fa));
        }

        let cond1 = (s - (3.0 * a + b) / 4.0) * (s - b) > 0.0;
        let cond2 = mflag && (s - b).abs() >= (b - c).abs() / 2.0;
        let cond3 = !mflag && (s - b).abs() >= (c - d).abs() / 2.0;

        if cond1 || cond2 || cond3 {
            s = (a + b) / 2.0;
            mflag = true;
        } else {
            mflag = false;
        }

        let fs = f(s);
        d = c;
        c = b;
        fc = fb;

        if fa * fs < 0.0 {
            b = s;
            fb = fs;
        } else {
            a = s;
            fa = fs;
        }

        if fa.abs() < fb.abs() {
            std::mem::swap(&mut a, &mut b);
            std::mem::swap(&mut fa, &mut fb);
        }
    }
    b
}

fn main() {
    let r = brent_root(|x| x * x - 2.0, 0.0, 2.0, 1e-10, 100);
    assert!((r - std::f64::consts::SQRT_2).abs() < 1e-8);
    println!("Rust Brent Root Finding verified.");
}
