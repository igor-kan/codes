package main

import (
	"fmt"
	"math"
)

func nevilleInterpolation(xs, ys []float64, x float64) float64 {
	n := len(xs)
	table := make([]float64, n)
	copy(table, ys)
	for k := 1; k < n; k++ {
		for i := 0; i < n-k; i++ {
			table[i] = ((x-xs[i+k])*table[i] + (xs[i]-x)*table[i+1]) / (xs[i] - xs[i+k])
		}
	}
	return table[0]
}

func main() {
	value := nevilleInterpolation([]float64{0, 1, 2}, []float64{1, 3, 2}, 1.5)
	if math.Abs(value-2.875) > 1e-12 {
		panic("neville failed")
	}
	fmt.Println("neville interpolation ok")
}
