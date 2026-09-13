//! Monotone Chain Convex Hull Algorithm in Rust.

#[derive(Copy, Clone, Debug, PartialEq)]
pub struct Point {
    pub x: f64,
    pub y: f64,
}

fn cross_product(o: Point, a: Point, b: Point) -> f64 {
    (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
}

pub fn convex_hull(mut pts: Vec<Point>) -> Vec<Point> {
    pts.sort_by(|a, b| {
        a.x.partial_cmp(&b.x).unwrap()
            .then_with(|| a.y.partial_cmp(&b.y).unwrap())
    });
    pts.dedup_by(|a, b| a.x == b.x && a.y == b.y);

    let n = pts.len();
    if n <= 1 {
        return pts;
    }

    let mut hull: Vec<Point> = Vec::new();

    // Lower hull
    for &p in &pts {
        while hull.len() >= 2 && cross_product(hull[hull.len() - 2], hull[hull.len() - 1], p) <= 0.0 {
            hull.pop();
        }
        hull.push(p);
    }

    // Upper hull
    let lower_len = hull.len();
    for &p in pts.iter().rev().skip(1) {
        while hull.len() > lower_len && cross_product(hull[hull.len() - 2], hull[hull.len() - 1], p) <= 0.0 {
            hull.pop();
        }
        hull.push(p);
    }

    hull.pop();
    hull
}

fn main() {
    let pts = vec![
        Point { x: 0.0, y: 3.0 }, Point { x: 2.0, y: 2.0 }, Point { x: 1.0, y: 1.0 }, Point { x: 2.0, y: 1.0 },
        Point { x: 3.0, y: 0.0 }, Point { x: 0.0, y: 0.0 }, Point { x: 3.0, y: 3.0 }, Point { x: 1.5, y: 1.5 },
    ];

    let hull = convex_hull(pts);
    assert_eq!(hull.len(), 4);
    assert_eq!(hull[0], Point { x: 0.0, y: 0.0 });
    assert_eq!(hull[1], Point { x: 3.0, y: 0.0 });
    assert_eq!(hull[2], Point { x: 3.0, y: 3.0 });
    assert_eq!(hull[3], Point { x: 0.0, y: 3.0 });

    println!("[Rust Convex Hull] Computed hull with {} vertices: {:?}", hull.len(), hull);
}
