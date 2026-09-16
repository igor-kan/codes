package main

import "fmt"

func runningSum(nums []int) []int {
	result := make([]int, len(nums))
	total := 0
	for i, value := range nums {
		total += value
		result[i] = total
	}
	return result
}

func main() {
	if fmt.Sprint(runningSum([]int{1, 2, 3, 4})) != "[1 3 6 10]" || fmt.Sprint(runningSum([]int{1, 1, 1, 1, 1})) != "[1 2 3 4 5]" {
		panic("running sum failed")
	}
	fmt.Println("1480 running sum ok")
}
