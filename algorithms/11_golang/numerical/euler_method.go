package main

import (
	"fmt"
	"math"
)

func eulerMethod(f func(float64, float64) float64, y0, t0, t1 float64, steps int) float64 {
	h := (t1 - t0) / float64(steps)
	y, t := y0, t0
	for i := 0; i < steps; i++ {
		y += h * f(t, y)
		t += h
	}
	return y
}

func main() {
	value := eulerMethod(func(t, y float64) float64 { return y }, 1, 0, 1, 1000)
	if math.Abs(value-math.E) > 0.01 {
		panic("euler method failed")
	}
	fmt.Println("euler method ok")
}
