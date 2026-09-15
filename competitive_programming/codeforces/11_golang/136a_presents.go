package main

import "fmt"

func presents(permutation []int) []int {
	result := make([]int, len(permutation))
	for index, giver := range permutation {
		result[giver-1] = index + 1
	}
	return result
}

func main() {
	got := presents([]int{2, 3, 4, 1})
	if got[0] != 4 || got[1] != 1 || got[2] != 2 || got[3] != 3 {
		panic("presents failed")
	}
	fmt.Println("136A presents ok")
}
