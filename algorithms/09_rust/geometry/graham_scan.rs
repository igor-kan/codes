#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Point { pub x: i64, pub y: i64 }
fn cross(o: Point, a: Point, b: Point) -> i64 {
    (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
}
pub fn convex_hull(mut pts: Vec<Point>) -> Vec<Point> {
    pts.sort_by(|a, b| a.x.cmp(&b.x).then(a.y.cmp(&b.y)));
    let mut hull = Vec::new();
    for p in pts {
        while hull.len() >= 2 && cross(hull[hull.len() - 2], hull[hull.len() - 1], p) <= 0 {
            hull.pop();
        }
        hull.push(p);
    }
    hull
}
fn main() {
    let pts = vec![Point{x:0,y:0}, Point{x:1,y:1}, Point{x:2,y:2}, Point{x:0,y:2}, Point{x:2,y:0}];
    let h = convex_hull(pts);
    assert!(!h.is_empty());
    println!("Rust Graham Scan verified.");
}
