package main

import "fmt"

func nextGreater(nums []int) []int {
	n := len(nums)
	res := make([]int, n)
	for i := range res {
		res[i] = -1
	}
	stack := make([]int, 0)
	for i := 0; i < n; i++ {
		for len(stack) > 0 && nums[stack[len(stack)-1]] < nums[i] {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			res[top] = nums[i]
		}
		stack = append(stack, i)
	}
	return res
}

func main() {
	nums := []int{2, 1, 2, 4, 3}
	got := nextGreater(nums)
	want := []int{4, 2, 4, -1, -1}
	for i := range want {
		if got[i] != want[i] {
			panic("monotonic stack: next greater mismatch")
		}
	}
	fmt.Println("[Go MonotonicStack] Next greater element verified:", got)
}
