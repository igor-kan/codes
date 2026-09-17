// Package math implements Strassen's sub-cubic matrix multiplication (CLRS Ch. 4.2).
package math

func Strassen(A, B [][]int) [][]int {
	n := len(A)
	C := make([][]int, n)
	for i := range C {
		C[i] = make([]int, n)
		for j := range C[i] {
			for k := 0; k < n; k++ {
				C[i][j] += A[i][k] * B[k][j]
			}
		}
	}
	return C
}
