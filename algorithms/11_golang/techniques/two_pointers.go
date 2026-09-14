package main

import "fmt"

func twoSumSorted(nums []int, target int) (int, int, bool) {
	i, j := 0, len(nums)-1
	for i < j {
		s := nums[i] + nums[j]
		if s == target {
			return i, j, true
		} else if s < target {
			i++
		} else {
			j--
		}
	}
	return -1, -1, false
}

func main() {
	nums := []int{-3, -1, 0, 2, 4, 7, 9}
	i, j, ok := twoSumSorted(nums, 6)
	if !ok || nums[i]+nums[j] != 6 {
		panic("two pointers: two-sum sorted failed")
	}
	if i != 0 || j != 6 {
		panic("two pointers: wrong indices")
	}
	fmt.Println("[Go TwoPointers] Sorted two-sum verified:", nums[i], "+", nums[j], "= 6")
}
