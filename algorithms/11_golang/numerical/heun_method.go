package main

import (
	"fmt"
	"math"
)

func heunMethod(f func(float64, float64) float64, y0, t0, t1 float64, steps int) float64 {
	h := (t1 - t0) / float64(steps)
	y, t := y0, t0
	for i := 0; i < steps; i++ {
		k1 := f(t, y)
		k2 := f(t+h, y+h*k1)
		y += 0.5 * h * (k1 + k2)
		t += h
	}
	return y
}

func main() {
	value := heunMethod(func(t, y float64) float64 { return y }, 1, 0, 1, 1000)
	if math.Abs(value-math.E) > 1e-4 {
		panic("heun method failed")
	}
	fmt.Println("heun method ok")
}
