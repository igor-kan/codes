package main

import "fmt"

func siftDown(a []int, root, end int) {
	for root*2+1 <= end {
		swap := root
		child := root*2 + 1
		if a[swap] < a[child] {
			swap = child
		}
		if child+1 <= end && a[swap] < a[child+1] {
			swap = child + 1
		}
		if swap == root {
			return
		}
		a[root], a[swap] = a[swap], a[root]
		root = swap
	}
}

func HeapSort(a []int) {
	n := len(a)
	if n <= 1 {
		return
	}
	for start := (n - 2) / 2; start >= 0; start-- {
		siftDown(a, start, n-1)
	}
	for end := n - 1; end > 0; end-- {
		a[0], a[end] = a[end], a[0]
		siftDown(a, 0, end-1)
	}
}

func main() {
	data := []int{33, 7, 91, 12, 5, 5, 78, 2, 44, 19}
	HeapSort(data)
	for i := 1; i < len(data); i++ {
		if data[i-1] > data[i] {
			panic("not sorted")
		}
	}
	fmt.Printf("[Go HeapSort] Sift-down heap sort verified: %v\n", data)
}
