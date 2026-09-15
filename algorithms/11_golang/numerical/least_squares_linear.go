package main

import (
	"fmt"
	"math"
)

func leastSquaresLinear(xs, ys []float64) (float64, float64) {
	n := float64(len(xs))
	meanX, meanY := 0.0, 0.0
	for i := range xs {
		meanX += xs[i] / n
		meanY += ys[i] / n
	}
	numerator, denominator := 0.0, 0.0
	for i := range xs {
		numerator += (xs[i] - meanX) * (ys[i] - meanY)
		denominator += (xs[i] - meanX) * (xs[i] - meanX)
	}
	slope := numerator / denominator
	return meanY - slope*meanX, slope
}

func main() {
	intercept, slope := leastSquaresLinear([]float64{0, 1, 2, 3}, []float64{1, 3, 5, 7})
	if math.Abs(intercept-1) > 1e-12 || math.Abs(slope-2) > 1e-12 {
		panic("least squares failed")
	}
	fmt.Println("least squares linear ok")
}
