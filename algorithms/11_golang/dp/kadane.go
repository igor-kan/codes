package main

import "fmt"

func maxSubarray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	best := nums[0]
	cur := nums[0]
	for i := 1; i < len(nums); i++ {
		if cur+nums[i] > nums[i] {
			cur = cur + nums[i]
		} else {
			cur = nums[i]
		}
		if cur > best {
			best = cur
		}
	}
	return best
}

func main() {
	nums := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	if maxSubarray(nums) != 6 {
		panic("Kadane: max subarray sum should be 6")
	}
	if maxSubarray([]int{-1, -2, -3}) != -1 {
		panic("Kadane: all-negative case failed")
	}
	fmt.Println("[Go Kadane] Maximum subarray sum verified: 6")
}
