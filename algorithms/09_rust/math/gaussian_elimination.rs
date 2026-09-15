//! Gaussian elimination with partial pivoting.
fn main() {
    let mut a = [
        [2.0_f64, 1.0, -1.0, 8.0],
        [-3.0, -1.0, 2.0, -11.0],
        [-2.0, 1.0, 2.0, -3.0],
    ];
    let n = 3;
    for c in 0..n {
        let mut p = c;
        for r in c + 1..n {
            if a[r][c].abs() > a[p][c].abs() {
                p = r;
            }
        }
        a.swap(c, p);
        for r in c + 1..n {
            let f = a[r][c] / a[c][c];
            for k in c..=n {
                a[r][k] -= f * a[c][k];
            }
        }
    }
    let mut x = [0.0_f64; 3];
    for r in (0..n).rev() {
        let mut s = a[r][n];
        for k in r + 1..n {
            s -= a[r][k] * x[k];
        }
        x[r] = s / a[r][r];
    }
    assert!((x[0] - 2.0).abs() < 1e-9 && (x[1] - 3.0).abs() < 1e-9 && (x[2] + 1.0).abs() < 1e-9);
    println!("x={} {} {}", x[0], x[1], x[2]);
}
