package main

import (
	"fmt"
	"math"
)

func thomasAlgorithm(lower, diagonal, upper, rhs []float64) []float64 {
	n := len(diagonal)
	c := make([]float64, n)
	d := make([]float64, n)
	c[0] = upper[0] / diagonal[0]
	d[0] = rhs[0] / diagonal[0]
	for i := 1; i < n; i++ {
		denominator := diagonal[i] - lower[i]*c[i-1]
		if i < n-1 {
			c[i] = upper[i] / denominator
		}
		d[i] = (rhs[i] - lower[i]*d[i-1]) / denominator
	}
	x := make([]float64, n)
	x[n-1] = d[n-1]
	for i := n - 2; i >= 0; i-- {
		x[i] = d[i] - c[i]*x[i+1]
	}
	return x
}

func main() {
	x := thomasAlgorithm([]float64{0, -1, -1}, []float64{2, 2, 2}, []float64{-1, -1, 0}, []float64{1, 0, 1})
	for _, value := range x {
		if math.Abs(value-1) > 1e-12 {
			panic("thomas failed")
		}
	}
	fmt.Println("thomas algorithm ok")
}
