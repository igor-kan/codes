package main

import "fmt"

func happyNumber(n int) bool {
	seen := map[int]bool{}
	for n != 1 && !seen[n] {
		seen[n] = true
		next := 0
		for _, digit := range fmt.Sprintf("%d", n) {
			value := int(digit - '0')
			next += value * value
		}
		n = next
	}
	return n == 1
}

func main() {
	if !happyNumber(19) || happyNumber(2) {
		panic("happy number failed")
	}
	fmt.Println("202 happy number ok")
}
