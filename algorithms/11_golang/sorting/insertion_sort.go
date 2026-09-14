package main

import "fmt"

func insertionSort(a []int) {
	for i := 1; i < len(a); i++ {
		key := a[i]
		j := i - 1
		for j >= 0 && a[j] > key {
			a[j+1] = a[j]
			j--
		}
		a[j+1] = key
	}
}

func main() {
	data := []int{33, 7, 91, 12, 5, 5, 78, 2, 44, 19}
	insertionSort(data)
	for i := 1; i < len(data); i++ {
		if data[i-1] > data[i] {
			panic("not sorted")
		}
	}
	fmt.Println("[Go InsertionSort] Insertion sort verified:", data)
}
