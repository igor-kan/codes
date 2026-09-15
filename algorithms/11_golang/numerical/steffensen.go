package main

import (
	"fmt"
	"math"
)

func steffensen(g func(float64) float64, x float64) float64 {
	for i := 0; i < 100; i++ {
		x1 := g(x)
		x2 := g(x1)
		denominator := x2 - 2*x1 + x
		if math.Abs(denominator) < 1e-15 {
			return x2
		}
		next := x - (x1-x)*(x1-x)/denominator
		if math.Abs(next-x) < 1e-12 {
			return next
		}
		x = next
	}
	return x
}

func main() {
	root := steffensen(func(x float64) float64 { return 0.5 * (x + 2/x) }, 1)
	if math.Abs(root-math.Sqrt2) > 1e-12 {
		panic("steffensen failed")
	}
	fmt.Println("steffensen ok")
}
