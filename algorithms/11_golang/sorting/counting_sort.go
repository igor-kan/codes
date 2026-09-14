package main

import "fmt"

func countingSort(a []int, maxVal int) []int {
	count := make([]int, maxVal+1)
	for _, v := range a {
		count[v]++
	}
	for i := 1; i <= maxVal; i++ {
		count[i] += count[i-1]
	}
	out := make([]int, len(a))
	for i := len(a) - 1; i >= 0; i-- {
		v := a[i]
		count[v]--
		out[count[v]] = v
	}
	return out
}

func main() {
	data := []int{4, 2, 2, 8, 3, 3, 1}
	sorted := countingSort(data, 8)
	want := []int{1, 2, 2, 3, 3, 4, 8}
	for i := range want {
		if sorted[i] != want[i] {
			panic("counting sort: mismatch")
		}
	}
	fmt.Println("[Go CountingSort] Counting sort verified:", sorted)
}
