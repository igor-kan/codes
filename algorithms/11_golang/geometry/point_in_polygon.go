// Ray-casting point-in-polygon test.
package main

import "fmt"

func inside(poly [][2]float64, px, py float64) bool {
	in := false
	n := len(poly)
	j := n - 1
	for i := 0; i < n; i++ {
		xi, yi := poly[i][0], poly[i][1]
		xj, yj := poly[j][0], poly[j][1]
		if (yi > py) != (yj > py) && px < (xj-xi)*(py-yi)/(yj-yi)+xi {
			in = !in
		}
		j = i
	}
	return in
}

func main() {
	square := [][2]float64{{0, 0}, {4, 0}, {4, 4}, {0, 4}}
	if !inside(square, 2, 2) || inside(square, 5, 5) {
		panic("ray casting failed")
	}
	fmt.Println("point in polygon ok")
}
