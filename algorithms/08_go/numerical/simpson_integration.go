package main

import (
	"fmt"
	"math"
)

func simpson(f func(float64) float64, a, b float64, n int) float64 {
	if n%2 == 1 {
		n++
	}
	h := (b - a) / float64(n)
	total := f(a) + f(b)
	for i := 1; i < n; i++ {
		if i%2 == 1 {
			total += 4 * f(a+float64(i)*h)
		} else {
			total += 2 * f(a+float64(i)*h)
		}
	}
	return total * h / 3
}

func main() {
	got := simpson(func(x float64) float64 { return x * x }, 0, 1, 1000)
	if math.Abs(got-1.0/3.0) > 1e-12 {
		panic("simpson mismatch")
	}
	fmt.Println("simpson integration ok")
}
