package main

import "fmt"

func zAlgorithm(s string) []int {
	n := len(s)
	z := make([]int, n)
	l, r := 0, 0
	for i := 1; i < n; i++ {
		if i <= r {
			if z[i-l] < r-i+1 {
				z[i] = z[i-l]
				continue
			}
			z[i] = r - i + 1
		}
		for i+z[i] < n && s[z[i]] == s[i+z[i]] {
			z[i]++
		}
		if i+z[i]-1 > r {
			l, r = i, i+z[i]-1
		}
	}
	return z
}

func main() {
	z := zAlgorithm("aaaa")
	want := []int{0, 3, 2, 1}
	for i := range want {
		if z[i] != want[i] {
			panic("Z-algorithm: mismatch")
		}
	}
	fmt.Println("[Go ZAlgorithm] Z-values verified.")
}
