package geometry
import "sort"
type Point struct{ X, Y int }
func cross(o, a, b Point) int { return (a.X-o.X)*(b.Y-o.Y) - (a.Y-o.Y)*(b.X-o.X) }
func GrahamScan(pts []Point) []Point {
    sort.Slice(pts, func(i, j int) bool {
        if pts[i].X == pts[j].X { return pts[i].Y < pts[j].Y }
        return pts[i].X < pts[j].X
    })
    hull := []Point{}
    for _, p := range pts {
        for len(hull) >= 2 && cross(hull[len(hull)-2], hull[len(hull)-1], p) <= 0 {
            hull = hull[:len(hull)-1]
        }
        hull = append(hull, p)
    }
    return hull
}
