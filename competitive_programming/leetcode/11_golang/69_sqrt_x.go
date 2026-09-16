package main

import "fmt"

func sqrtX(x int) int {
	low, high := 0, x
	for low <= high {
		middle := (low + high) / 2
		if middle*middle <= x {
			low = middle + 1
		} else {
			high = middle - 1
		}
	}
	return high
}

func main() {
	if sqrtX(4) != 2 || sqrtX(8) != 2 || sqrtX(0) != 0 {
		panic("sqrt x failed")
	}
	fmt.Println("69 sqrt x ok")
}
