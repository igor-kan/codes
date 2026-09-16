package main

import "fmt"

func searchInsert(nums []int, target int) int {
	low, high := 0, len(nums)
	for low < high {
		middle := (low + high) / 2
		if nums[middle] < target {
			low = middle + 1
		} else {
			high = middle
		}
	}
	return low
}

func main() {
	if searchInsert([]int{1, 3, 5, 6}, 5) != 2 || searchInsert([]int{1, 3, 5, 6}, 2) != 1 {
		panic("search insert failed")
	}
	if searchInsert([]int{1, 3, 5, 6}, 7) != 4 || searchInsert([]int{1, 3, 5, 6}, 0) != 0 {
		panic("search insert failed")
	}
	fmt.Println("35 search insert position ok")
}
