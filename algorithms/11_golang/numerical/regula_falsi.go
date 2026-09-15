package main

import (
	"fmt"
	"math"
)

func regulaFalsi(f func(float64) float64, a, b float64) float64 {
	fa, fb := f(a), f(b)
	if fa*fb > 0 {
		panic("root is not bracketed")
	}
	c := a
	for i := 0; i < 200; i++ {
		c = (a*fb - b*fa) / (fb - fa)
		fc := f(c)
		if math.Abs(fc) < 1e-12 {
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
	root := regulaFalsi(func(x float64) float64 { return x*x - 2 }, 0, 2)
	if math.Abs(root-math.Sqrt2) > 1e-9 {
		panic("regula falsi failed")
	}
	fmt.Println("regula falsi ok")
}
