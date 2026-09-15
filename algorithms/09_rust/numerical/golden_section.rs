//! Golden-section search for a 1D minimum (Numerical Recipes 10.1).
fn golden_section(f: impl Fn(f64) -> f64, mut a: f64, mut b: f64) -> f64 {
    let inv_phi = (5f64.sqrt() - 1.0) / 2.0;
    let mut c = b - inv_phi * (b - a);
    let mut d = a + inv_phi * (b - a);
    let mut fc = f(c);
    let mut fd = f(d);
    while b - a > 1e-9 {
        if fc < fd {
            b = d;
            d = c;
            fd = fc;
            c = b - inv_phi * (b - a);
            fc = f(c);
        } else {
            a = c;
            c = d;
            fc = fd;
            d = a + inv_phi * (b - a);
            fd = f(d);
        }
    }
    (a + b) / 2.0
}

fn main() {
    let x = golden_section(|x| (x - 3.0) * (x - 3.0), -10.0, 10.0);
    assert!((x - 3.0).abs() < 1e-6);
    println!("golden section ok");
}
