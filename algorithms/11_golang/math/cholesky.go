// Package math implements Cholesky LL^T decomposition (Numerical Recipes Ch. 2.6).
package math

import "math"

func Cholesky(A [][]float64) [][]float64 {
	n := len(A)
	L := make([][]float64, n)
	for i := range L {
		L[i] = make([]float64, n)
	}

	for i := 0; i < n; i++ {
		for j := 0; j <= i; j++ {
			sum := 0.0
			for k := 0; k < j; k++ {
				sum += L[i][k] * L[j][k]
			}
			if i == j {
				val := A[i][i] - sum
				if val <= 0 {
					panic("matrix not positive definite")
				}
				L[i][j] = math.Sqrt(val)
			} else {
				L[i][j] = (A[i][j] - sum) / L[j][j]
			}
		}
	}
	return L
}
