// Package math implements Conjugate Gradient linear solver (Numerical Recipes Ch. 2.7).
package math

import "math"

func dot(a, b []float64) float64 {
	sum := 0.0
	for i := range a {
		sum += a[i] * b[i]
	}
	return sum
}

func matVec(A [][]float64, v []float64) []float64 {
	res := make([]float64, len(A))
	for i := range A {
		res[i] = dot(A[i], v)
	}
	return res
}

func ConjugateGradient(A [][]float64, b []float64, tol float64, maxIter int) []float64 {
	n := len(b)
	x := make([]float64, n)
	r := make([]float64, n)
	copy(r, b)
	p := make([]float64, n)
	copy(p, r)
	rsOld := dot(r, r)

	for iter := 0; iter < maxIter; iter++ {
		if math.Sqrt(rsOld) < tol {
			break
		}
		Ap := matVec(A, p)
		alpha := rsOld / dot(p, Ap)

		for i := 0; i < n; i++ {
			x[i] += alpha * p[i]
			r[i] -= alpha * Ap[i]
		}
		rsNew := dot(r, r)
		for i := 0; i < n; i++ {
			p[i] = r[i] + (rsNew/rsOld)*p[i]
		}
		rsOld = rsNew
	}
	return x
}
