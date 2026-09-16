package main

import "fmt"

func removeElement(nums []int, value int) []int {
	result := []int{}
	for _, number := range nums {
		if number != value {
			result = append(result, number)
		}
	}
	return result
}

func main() {
	if fmt.Sprint(removeElement([]int{3, 2, 2, 3}, 3)) != "[2 2]" {
		panic("remove element failed")
	}
	if fmt.Sprint(removeElement([]int{0, 1, 2, 2, 3, 0, 4, 2}, 2)) != "[0 1 3 0 4]" {
		panic("remove element failed")
	}
	fmt.Println("27 remove element ok")
}
