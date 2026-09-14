package main

import "fmt"

func subsets(nums []int) [][]int {
	res := [][]int{}
	cur := []int{}
	var dfs func(start int)
	dfs = func(start int) {
		cp := make([]int, len(cur))
		copy(cp, cur)
		res = append(res, cp)
		for i := start; i < len(nums); i++ {
			cur = append(cur, nums[i])
			dfs(i + 1)
			cur = cur[:len(cur)-1]
		}
	}
	dfs(0)
	return res
}

func permutations(nums []int) [][]int {
	res := [][]int{}
	cur := []int{}
	used := make([]bool, len(nums))
	var dfs func()
	dfs = func() {
		if len(cur) == len(nums) {
			cp := make([]int, len(cur))
			copy(cp, cur)
			res = append(res, cp)
			return
		}
		for i := 0; i < len(nums); i++ {
			if used[i] {
				continue
			}
			used[i] = true
			cur = append(cur, nums[i])
			dfs()
			cur = cur[:len(cur)-1]
			used[i] = false
		}
	}
	dfs()
	return res
}

func main() {
	s := subsets([]int{1, 2, 3})
	if len(s) != 8 {
		panic("backtracking: subsets count should be 8")
	}
	p := permutations([]int{1, 2, 3})
	if len(p) != 6 {
		panic("backtracking: permutations count should be 6")
	}
	fmt.Println("[Go Backtracking] Subsets (8) + permutations (6) verified.")
}
