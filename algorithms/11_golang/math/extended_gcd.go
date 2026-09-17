// Package math implements Extended Euclidean Algorithm (CLRS 3rd Ed. Chapter 31.2).
package math

func ExtendedGCD(a, b int64) (gcd, x, y int64) {
	if b == 0 {
		return a, 1, 0
	}
	gcd, x1, y1 := ExtendedGCD(b, a%b)
	x = y1
	y = x1 - (a/b)*y1
	return gcd, x, y
}
