package main

import (
	"fmt"
	"math"
)

func linearInterpolation(xs, ys []float64, x float64) float64 {
	if x <= xs[0] {
		return ys[0]
	}
	if x >= xs[len(xs)-1] {
		return ys[len(ys)-1]
	}
	for i := 1; i < len(xs); i++ {
		if x <= xs[i] {
			slope := (ys[i] - ys[i-1]) / (xs[i] - xs[i-1])
			return ys[i-1] + slope*(x-xs[i-1])
		}
	}
	return ys[len(ys)-1]
}

func main() {
	if math.Abs(linearInterpolation([]float64{0, 1, 2}, []float64{0, 2, 4}, 0.5)-1) > 1e-12 {
		panic("linear failed")
	}
	if math.Abs(linearInterpolation([]float64{0, 1, 4}, []float64{0, 1, 2}, 2.5)-1.5) > 1e-12 {
		panic("linear segment failed")
	}
	fmt.Println("linear interpolation ok")
}
