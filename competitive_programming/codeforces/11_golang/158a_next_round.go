package main

import "fmt"

func nextRound(scores []int, k int) int {
	threshold := scores[k-1]
	count := 0
	for _, score := range scores {
		if score >= threshold && score > 0 {
			count++
		}
	}
	return count
}

func main() {
	if nextRound([]int{10, 9, 8, 7, 7, 7, 5, 5}, 5) != 6 || nextRound([]int{0, 0, 0, 0}, 2) != 0 {
		panic("next round failed")
	}
	fmt.Println("158A next round ok")
}
