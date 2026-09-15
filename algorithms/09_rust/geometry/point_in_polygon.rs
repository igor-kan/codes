//! Ray-casting point-in-polygon test.
fn inside(poly: &[(f64, f64)], px: f64, py: f64) -> bool {
    let n = poly.len();
    let mut inside = false;
    let mut j = n - 1;
    for i in 0..n {
        let (xi, yi) = poly[i];
        let (xj, yj) = poly[j];
        if ((yi > py) != (yj > py)) && (px < (xj - xi) * (py - yi) / (yj - yi) + xi) {
            inside = !inside;
        }
        j = i;
    }
    inside
}

fn main() {
    let square = [(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0)];
    assert!(inside(&square, 2.0, 2.0));
    assert!(!inside(&square, 5.0, 5.0));
    println!("point in polygon ok");
}
