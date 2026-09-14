package main

import "fmt"

func lis(nums []int) int {
	tails := []int{}
	for _, x := range nums {
		lo, hi := 0, len(tails)
		for lo < hi {
			mid := (lo + hi) / 2
			if tails[mid] < x {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		if lo == len(tails) {
			tails = append(tails, x)
		} else {
			tails[lo] = x
		}
	}
	return len(tails)
}

func main() {
	nums := []int{10, 9, 2, 5, 3, 7, 101, 18}
	if lis(nums) != 4 {
		panic("LIS: length should be 4")
	}
	if lis([]int{1, 2, 3, 4}) != 4 || lis([]int{4, 3, 2, 1}) != 1 {
		panic("LIS: edge cases failed")
	}
	fmt.Println("[Go LIS] O(n log n) length verified: 4")
}
