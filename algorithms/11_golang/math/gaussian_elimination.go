// Gaussian elimination with partial pivoting.
package main

import (
	"fmt"
	"math"
)

func main() {
	a := [][]float64{{2, 1, -1, 8}, {-3, -1, 2, -11}, {-2, 1, 2, -3}}
	n := 3
	for c := 0; c < n; c++ {
		p := c
		for r := c + 1; r < n; r++ {
			if math.Abs(a[r][c]) > math.Abs(a[p][c]) {
				p = r
			}
		}
		a[c], a[p] = a[p], a[c]
		for r := c + 1; r < n; r++ {
			f := a[r][c] / a[c][c]
			for k := c; k <= n; k++ {
				a[r][k] -= f * a[c][k]
			}
		}
	}
	x := make([]float64, n)
	for r := n - 1; r >= 0; r-- {
		s := a[r][n]
		for k := r + 1; k < n; k++ {
			s -= a[r][k] * x[k]
		}
		x[r] = s / a[r][r]
	}
	if math.Abs(x[0]-2) > 1e-9 || math.Abs(x[1]-3) > 1e-9 || math.Abs(x[2]+1) > 1e-9 {
		panic("wrong solution")
	}
	fmt.Println("x=", x)
}
