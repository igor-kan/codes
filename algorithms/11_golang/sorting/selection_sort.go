package main

import "fmt"

func selectionSort(a []int) {
	for i := 0; i < len(a)-1; i++ {
		minIdx := i
		for j := i + 1; j < len(a); j++ {
			if a[j] < a[minIdx] {
				minIdx = j
			}
		}
		a[i], a[minIdx] = a[minIdx], a[i]
	}
}

func main() {
	data := []int{33, 7, 91, 12, 5, 5, 78, 2, 44, 19}
	selectionSort(data)
	for i := 1; i < len(data); i++ {
		if data[i-1] > data[i] {
			panic("not sorted")
		}
	}
	fmt.Println("[Go SelectionSort] Selection sort verified:", data)
}
