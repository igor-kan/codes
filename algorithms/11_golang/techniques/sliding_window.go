package main

import "fmt"

func maxSumFixedWindow(nums []int, k int) int {
	if k > len(nums) {
		return 0
	}
	sum := 0
	for i := 0; i < k; i++ {
		sum += nums[i]
	}
	best := sum
	for i := k; i < len(nums); i++ {
		sum += nums[i] - nums[i-k]
		if sum > best {
			best = sum
		}
	}
	return best
}

func main() {
	nums := []int{2, 1, 5, 1, 3, 2}
	if maxSumFixedWindow(nums, 3) != 9 {
		panic("sliding window: fixed-size max sum failed")
	}
	fmt.Println("[Go SlidingWindow] Fixed-size max sum verified: 9")
}
