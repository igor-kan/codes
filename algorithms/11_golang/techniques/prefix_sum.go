package main

import "fmt"

func prefixSums(nums []int) []int {
	pref := make([]int, len(nums)+1)
	for i, v := range nums {
		pref[i+1] = pref[i] + v
	}
	return pref
}

func rangeSum(pref []int, l, r int) int {
	return pref[r+1] - pref[l]
}

func main() {
	nums := []int{3, 1, 4, 1, 5, 9, 2, 6}
	pref := prefixSums(nums)
	if rangeSum(pref, 2, 4) != 10 { // 4 + 1 + 5
		panic("prefix sum: range [2,4] should be 10")
	}
	if rangeSum(pref, 0, len(nums)-1) != 31 {
		panic("prefix sum: total should be 31")
	}
	fmt.Println("[Go PrefixSum] Range sum queries verified.")
}
