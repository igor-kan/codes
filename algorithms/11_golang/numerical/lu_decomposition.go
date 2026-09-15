package main

import (
	"fmt"
	"math"
)

func luSolve(a [][]float64, b []float64) []float64 {
	n := len(a)
	for col := 0; col < n; col++ {
		pivot := col
		for r := col + 1; r < n; r++ {
			if math.Abs(a[r][col]) > math.Abs(a[pivot][col]) {
				pivot = r
			}
		}
		a[col], a[pivot] = a[pivot], a[col]
		b[col], b[pivot] = b[pivot], b[col]
		for r := col + 1; r < n; r++ {
			f := a[r][col] / a[col][col]
			for k := col; k < n; k++ {
				a[r][k] -= f * a[col][k]
			}
			b[r] -= f * b[col]
		}
	}
	x := make([]float64, n)
	for r := n - 1; r >= 0; r-- {
		s := b[r]
		for k := r + 1; k < n; k++ {
			s -= a[r][k] * x[k]
		}
		x[r] = s / a[r][r]
	}
	return x
}

func main() {
	x := luSolve([][]float64{{2, 1, -1}, {-3, -1, 2}, {-2, 1, 2}}, []float64{8, -11, -3})
	if math.Abs(x[0]-2) > 1e-9 || math.Abs(x[1]-3) > 1e-9 || math.Abs(x[2]+1) > 1e-9 {
		panic("lu decomposition mismatch")
	}
	fmt.Println("lu decomposition ok")
}
