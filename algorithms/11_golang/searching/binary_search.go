package main

import "fmt"

func lowerBound(a []int, x int) int {
	lo, hi := 0, len(a)
	for lo < hi {
		mid := (lo + hi) / 2
		if a[mid] < x {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}

func upperBound(a []int, x int) int {
	lo, hi := 0, len(a)
	for lo < hi {
		mid := (lo + hi) / 2
		if a[mid] <= x {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}

func feasible(cap int) bool {
	// Example: can we split workloads of [3,2,2,4,1,4] into 3 groups
	// each with sum <= cap?
	workloads := []int{3, 2, 2, 4, 1, 4}
	groups := 0
	cur := 0
	for _, w := range workloads {
		if w > cap {
			return false
		}
		if cur+w > cap {
			groups++
			cur = w
		} else {
			cur += w
		}
	}
	groups++
	return groups <= 3
}

func main() {
	a := []int{1, 2, 2, 3, 3, 3, 5}
	if lowerBound(a, 3) != 3 || lowerBound(a, 0) != 0 || lowerBound(a, 6) != 7 {
		panic("lower_bound failed")
	}
	if upperBound(a, 3) != 6 || upperBound(a, 0) != 0 || upperBound(a, 5) != 7 {
		panic("upper_bound failed")
	}

	// Binary search on answer: minimal capacity for 3 groups is 6.
	lo, hi := 0, 16
	for lo < hi {
		mid := (lo + hi) / 2
		if feasible(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	if lo != 6 {
		panic("binary search on answer failed")
	}
	fmt.Println("[Go BinarySearch] lower_bound/upper_bound + answer search verified.")
}
