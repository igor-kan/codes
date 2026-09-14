package main

import "fmt"

const mod = 1_000_000_007

func modPow(a, b, m int) int {
	a %= m
	res := 1
	for b > 0 {
		if b&1 == 1 {
			res = res * a % m
		}
		a = a * a % m
		b >>= 1
	}
	return res
}

var fact, invFact []int

func initFact(n int) {
	fact = make([]int, n+1)
	invFact = make([]int, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * i % mod
	}
	invFact[n] = modPow(fact[n], mod-2, mod)
	for i := n - 1; i >= 0; i-- {
		invFact[i] = invFact[i+1] * (i + 1) % mod
	}
}

func nCr(n, r int) int {
	if r < 0 || r > n {
		return 0
	}
	return fact[n] * invFact[r] % mod * invFact[n-r] % mod
}

func main() {
	initFact(100)
	if nCr(5, 2) != 10 || nCr(10, 3) != 120 || nCr(10, 10) != 1 {
		panic("nCr mod p failed")
	}
	fmt.Println("[Go nCr] Binomial coefficients mod p verified.")
}
