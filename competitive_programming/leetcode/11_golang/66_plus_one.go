package main

import "fmt"

func plusOne(digits []int) []int {
	result := append([]int{}, digits...)
	for i := len(result) - 1; i >= 0; i-- {
		if result[i] < 9 {
			result[i]++
			return result
		}
		result[i] = 0
	}
	return append([]int{1}, result...)
}

func main() {
	if fmt.Sprint(plusOne([]int{1, 2, 3})) != "[1 2 4]" || fmt.Sprint(plusOne([]int{9, 9})) != "[1 0 0]" {
		panic("plus one failed")
	}
	fmt.Println("66 plus one ok")
}
