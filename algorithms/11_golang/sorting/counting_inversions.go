package main

import "fmt"

func mergeCount(a, buf []int, lo, hi int) int {
	if hi-lo <= 1 {
		return 0
	}
	mid := (lo + hi) / 2
	inversions := mergeCount(a, buf, lo, mid) + mergeCount(a, buf, mid, hi)
	i, j, k := lo, mid, lo
	for i < mid && j < hi {
		if a[i] <= a[j] {
			buf[k] = a[i]
			i++
		} else {
			buf[k] = a[j]
			j++
			inversions += mid - i
		}
		k++
	}
	for i < mid {
		buf[k] = a[i]
		i++
		k++
	}
	for j < hi {
		buf[k] = a[j]
		j++
		k++
	}
	copy(a[lo:hi], buf[lo:hi])
	return inversions
}

func countInversions(a []int) int {
	buf := make([]int, len(a))
	return mergeCount(a, buf, 0, len(a))
}

func main() {
	if countInversions([]int{2, 4, 1, 3, 5}) != 3 || countInversions([]int{5, 4, 3, 2, 1}) != 10 {
		panic("counting inversions mismatch")
	}
	fmt.Println("counting inversions ok")
}
