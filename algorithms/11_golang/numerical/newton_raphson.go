package main

import (
	"fmt"
	"math"
)

func newton(f, df func(float64) float64, x float64) float64 {
	for i := 0; i < 100; i++ {
		fx := f(x)
		if math.Abs(fx) < 1e-12 {
			break
		}
		x -= fx / df(x)
	}
	return x
}

func main() {
	root := newton(func(x float64) float64 { return x*x - 2 }, func(x float64) float64 { return 2 * x }, 1)
	if math.Abs(root-math.Sqrt2) > 1e-9 {
		panic("newton-raphson mismatch")
	}
	fmt.Println("newton-raphson ok")
}
