package main

import "fmt"

func cutRod(prices []int, n int) int {
	best := make([]int, n+1)
	for length := 1; length <= n; length++ {
		for i := 1; i <= length; i++ {
			if v := prices[i-1] + best[length-i]; v > best[length] {
				best[length] = v
			}
		}
	}
	return best[n]
}

func main() {
	prices := []int{1, 5, 8, 9, 10, 17, 17, 20, 24, 30}
	if cutRod(prices, 4) != 10 || cutRod(prices, 7) != 18 || cutRod(prices, 10) != 30 {
		panic("rod cutting mismatch")
	}
	fmt.Println("rod cutting ok")
}
