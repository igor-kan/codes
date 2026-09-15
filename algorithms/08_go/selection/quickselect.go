package main

import (
	"fmt"
	"sort"
)

func quickselect(a []int, k int) int {
	lo, hi := 0, len(a)-1
	for {
		pivot, i := a[hi], lo
		for j := lo; j < hi; j++ {
			if a[j] < pivot {
				a[i], a[j] = a[j], a[i]
				i++
			}
		}
		a[i], a[hi] = a[hi], a[i]
		if i == k {
			return a[i]
		}
		if k < i {
			hi = i - 1
		} else {
			lo = i + 1
		}
	}
}

func main() {
	data := []int{3, 2, 1, 5, 6, 4}
	sorted := append([]int(nil), data...)
	sort.Ints(sorted)
	for k := range data {
		got := quickselect(append([]int(nil), data...), k)
		if got != sorted[k] {
			panic("quickselect mismatch")
		}
	}
	fmt.Println("quickselect ok")
}
