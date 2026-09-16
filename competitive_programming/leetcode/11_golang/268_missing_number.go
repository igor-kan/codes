package main

import "fmt"

func missingNumber(nums []int) int {
	n := len(nums)
	total := n * (n + 1) / 2
	for _, value := range nums {
		total -= value
	}
	return total
}

func main() {
	if missingNumber([]int{3, 0, 1}) != 2 || missingNumber([]int{9, 6, 4, 2, 3, 5, 7, 0, 1}) != 8 {
		panic("missing number failed")
	}
	fmt.Println("268 missing number ok")
}
