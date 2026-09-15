package main

import (
	"fmt"
	"math"
)

func fixedPoint(g func(float64) float64, x float64) float64 {
	for i := 0; i < 200; i++ {
		next := g(x)
		if math.Abs(next-x) < 1e-12 {
			return next
		}
		x = next
	}
	return x
}

func main() {
	root := fixedPoint(func(x float64) float64 { return 0.5 * (x + 2/x) }, 1)
	if math.Abs(root-math.Sqrt2) > 1e-9 {
		panic("fixed point failed")
	}
	fmt.Println("fixed point ok")
}
