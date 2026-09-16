package main

import "fmt"

func moveZeroes(nums []int) []int {
	result := []int{}
	for _, number := range nums {
		if number != 0 {
			result = append(result, number)
		}
	}
	for len(result) < len(nums) {
		result = append(result, 0)
	}
	return result
}

func main() {
	if fmt.Sprint(moveZeroes([]int{0, 1, 0, 3, 12})) != "[1 3 12 0 0]" || fmt.Sprint(moveZeroes([]int{0})) != "[0]" {
		panic("move zeroes failed")
	}
	fmt.Println("283 move zeroes ok")
}
