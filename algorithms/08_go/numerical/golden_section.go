package main

import (
	"fmt"
	"math"
)

func goldenSection(f func(float64) float64, a, b float64) float64 {
	invPhi := (math.Sqrt(5) - 1) / 2
	c := b - invPhi*(b-a)
	d := a + invPhi*(b-a)
	fc, fd := f(c), f(d)
	for b-a > 1e-9 {
		if fc < fd {
			b = d
			d = c
			fd = fc
			c = b - invPhi*(b-a)
			fc = f(c)
		} else {
			a = c
			c = d
			fc = fd
			d = a + invPhi*(b-a)
			fd = f(d)
		}
	}
	return (a + b) / 2
}

func main() {
	x := goldenSection(func(x float64) float64 { return (x - 3) * (x - 3) }, -10, 10)
	if math.Abs(x-3) > 1e-6 {
		panic("golden section mismatch")
	}
	fmt.Println("golden section ok")
}
