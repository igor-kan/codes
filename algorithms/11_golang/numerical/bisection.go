package main

import (
	"fmt"
	"math"
)

func bisection(f func(float64) float64, a, b float64) float64 {
	fa, fb := f(a), f(b)
	if fa*fb > 0 {
		panic("root is not bracketed")
	}
	c := a
	for i := 0; i < 200; i++ {
		c = 0.5 * (a + b)
		fc := f(c)
		if fc == 0 || (b-a)/2 < 1e-12 {
			return c
		}
		if fa*fc < 0 {
			b, fb = c, fc
		} else {
			a, fa = c, fc
		}
	}
	return c
}

func main() {
	root := bisection(func(x float64) float64 { return x*x - 2 }, 0, 2)
	if math.Abs(root-math.Sqrt2) > 1e-9 {
		panic("bisection failed")
	}
	fmt.Println("bisection ok")
}
