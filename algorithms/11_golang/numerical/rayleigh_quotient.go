package main

import (
	"fmt"
	"math"
)

func rayleighQuotient(matrix [][]float64, vector []float64) float64 {
	n := len(matrix)
	scale := 0.0
	for _, value := range vector {
		scale = math.Max(scale, math.Abs(value))
	}
	x := make([]float64, n)
	for i := range vector {
		x[i] = vector[i] / scale
	}
	eigenvalue := 0.0
	for iteration := 0; iteration < 100; iteration++ {
		product := make([]float64, n)
		norm := 0.0
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				product[i] += matrix[i][j] * x[j]
			}
			norm = math.Max(norm, math.Abs(product[i]))
		}
		for i := 0; i < n; i++ {
			x[i] = product[i] / norm
		}
		numerator, denominator := 0.0, 0.0
		for i := 0; i < n; i++ {
			ax := 0.0
			for j := 0; j < n; j++ {
				ax += matrix[i][j] * x[j]
			}
			numerator += x[i] * ax
			denominator += x[i] * x[i]
		}
		next := numerator / denominator
		if math.Abs(next-eigenvalue) < 1e-12 {
			return next
		}
		eigenvalue = next
	}
	return eigenvalue
}

func main() {
	eigenvalue := rayleighQuotient([][]float64{{2, 1}, {1, 2}}, []float64{1, 0})
	if math.Abs(eigenvalue-3) > 1e-9 {
		panic("rayleigh failed")
	}
	fmt.Println("rayleigh quotient ok")
}
