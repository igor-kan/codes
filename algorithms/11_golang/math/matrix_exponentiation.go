// Fibonacci by matrix exponentiation.
package main

import "fmt"

type matrix [2][2]int64

func mul(a, b matrix) matrix {
	var r matrix
	for i := 0; i < 2; i++ {
		for j := 0; j < 2; j++ {
			for k := 0; k < 2; k++ {
				r[i][j] += a[i][k] * b[k][j]
			}
		}
	}
	return r
}

func fib(n int) int64 {
	r := matrix{{1, 0}, {0, 1}}
	m := matrix{{1, 1}, {1, 0}}
	for n > 0 {
		if n&1 == 1 {
			r = mul(r, m)
		}
		m = mul(m, m)
		n >>= 1
	}
	return r[0][1]
}

func main() {
	if fib(10) != 55 || fib(20) != 6765 {
		panic("wrong Fibonacci")
	}
	fmt.Println("fib(20)=", fib(20))
}
