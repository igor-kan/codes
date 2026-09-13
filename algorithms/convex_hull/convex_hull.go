package main

import (
	"fmt"
	"sort"
)

type Point struct {
	X, Y float64
}

func crossProduct(o, a, b Point) float64 {
	return (a.X-o.X)*(b.Y-o.Y) - (a.Y-o.Y)*(b.X-o.X)
}

func ConvexHull(pts []Point) []Point {
	sort.Slice(pts, func(i, j int) bool {
		if pts[i].X != pts[j].X {
			return pts[i].X < pts[j].X
		}
		return pts[i].Y < pts[j].Y
	})

	n := len(pts)
	if n <= 1 {
		return pts
	}

	hull := make([]Point, 0)

	// Lower hull
	for _, p := range pts {
		for len(hull) >= 2 && crossProduct(hull[len(hull)-2], hull[len(hull)-1], p) <= 0 {
			hull = hull[:len(hull)-1]
		}
		hull = append(hull, p)
	}

	// Upper hull
	lowerLen := len(hull)
	for i := n - 2; i >= 0; i-- {
		p := pts[i]
		for len(hull) > lowerLen && crossProduct(hull[len(hull)-2], hull[len(hull)-1], p) <= 0 {
			hull = hull[:len(hull)-1]
		}
		hull = append(hull, p)
	}

	return hull[:len(hull)-1]
}

func main() {
	pts := []Point{
		{0.0, 3.0}, {2.0, 2.0}, {1.0, 1.0}, {2.0, 1.0},
		{3.0, 0.0}, {0.0, 0.0}, {3.0, 3.0}, {1.5, 1.5},
	}

	hull := ConvexHull(pts)
	if len(hull) != 4 {
		panic(fmt.Sprintf("Expected 4 vertices, got %d", len(hull)))
	}

	fmt.Printf("[Go Convex Hull] Hull computed successfully with %d vertices.\n", len(hull))
}
