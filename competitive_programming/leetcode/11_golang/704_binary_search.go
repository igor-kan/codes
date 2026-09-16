package main

import "fmt"

func binarySearch(nums []int, target int) int {
	low, high := 0, len(nums)-1
	for low <= high {
		middle := (low + high) / 2
		if nums[middle] == target {
			return middle
		}
		if nums[middle] < target {
			low = middle + 1
		} else {
			high = middle - 1
		}
	}
	return -1
}

func main() {
	if binarySearch([]int{-1, 0, 3, 5, 9, 12}, 9) != 4 || binarySearch([]int{-1, 0, 3, 5, 9, 12}, 2) != -1 {
		panic("binary search failed")
	}
	fmt.Println("704 binary search ok")
}
