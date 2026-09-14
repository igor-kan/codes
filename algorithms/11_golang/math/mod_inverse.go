package main

import "fmt"

func modPow(a, b, mod int) int {
	a %= mod
	res := 1
	for b > 0 {
		if b&1 == 1 {
			res = res * a % mod
		}
		a = a * a % mod
		b >>= 1
	}
	return res
}

func egcd(a, b int) (int, int) {
	if b == 0 {
		return 1, 0
	}
	x, y := egcd(b, a%b)
	return y, x - (a/b)*y
}

func modInverseExt(a, mod int) int {
	x, _ := egcd(a, mod)
	return ((x % mod) + mod) % mod
}

func modInverseFermat(a, mod int) int {
	return modPow(a, mod-2, mod)
}

func main() {
	const mod = 1_000_000_007
	if modInverseFermat(3, mod) != 333333336 {
		panic("mod inverse (Fermat) failed")
	}
	if modInverseExt(3, mod) != 333333336 {
		panic("mod inverse (Euclid) failed")
	}
	if 3*modInverseExt(3, mod)%mod != 1 {
		panic("mod inverse: product should be 1 mod p")
	}
	fmt.Println("[Go ModInverse] Extended Euclid + Fermat verified.")
}
