package main

import "fmt"

func removeDuplicates(nums []int) []int {
	result := []int{}
	for _, value := range nums {
		if len(result) == 0 || result[len(result)-1] != value {
			result = append(result, value)
		}
	}
	return result
}

func main() {
	if fmt.Sprint(removeDuplicates([]int{1, 1, 2})) != "[1 2]" {
		panic("remove duplicates failed")
	}
	if fmt.Sprint(removeDuplicates([]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4})) != "[0 1 2 3 4]" {
		panic("remove duplicates failed")
	}
	fmt.Println("26 remove duplicates ok")
}
