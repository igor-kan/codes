package main

import "fmt"

func reverseInteger(x int) int {
	sign := 1
	if x < 0 {
		sign = -1
	}
	value := x * sign
	reversed := 0
	for value > 0 {
		reversed = reversed*10 + value%10
		value /= 10
	}
	reversed *= sign
	if reversed < -(1<<31) || reversed > (1<<31)-1 {
		return 0
	}
	return reversed
}

func main() {
	if reverseInteger(123) != 321 || reverseInteger(-123) != -321 || reverseInteger(120) != 21 {
		panic("reverse integer failed")
	}
	if reverseInteger(1534236469) != 0 {
		panic("reverse integer overflow failed")
	}
	fmt.Println("7 reverse integer ok")
}
