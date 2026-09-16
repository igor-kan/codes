package main

import "fmt"

func containsDuplicate(nums []int) bool {
	seen := map[int]bool{}
	for _, value := range nums {
		if seen[value] {
			return true
		}
		seen[value] = true
	}
	return false
}

func main() {
	if !containsDuplicate([]int{1, 2, 3, 1}) || containsDuplicate([]int{1, 2, 3, 4}) {
		panic("contains duplicate failed")
	}
	fmt.Println("217 contains duplicate ok")
}
