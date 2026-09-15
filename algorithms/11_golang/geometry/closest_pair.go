// Closest pair of points (quadratic brute force).
package main

import (
	"fmt"
	"math"
)

func main() {
	pts := [][2]float64{{2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}}
	best := math.Inf(1)
	for i := 0; i < len(pts); i++ {
		for j := i + 1; j < len(pts); j++ {
			d := math.Hypot(pts[i][0]-pts[j][0], pts[i][1]-pts[j][1])
			if d < best {
				best = d
			}
		}
	}
	if math.Abs(best-math.Sqrt2) > 1e-9 {
		panic("wrong closest distance")
	}
	fmt.Println("closest=", best)
}
