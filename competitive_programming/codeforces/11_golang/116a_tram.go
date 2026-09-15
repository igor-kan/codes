package main

import "fmt"

func tram(stops [][2]int) int {
	current, capacity := 0, 0
	for _, stop := range stops {
		current = current - stop[0] + stop[1]
		if current > capacity {
			capacity = current
		}
	}
	return capacity
}

func main() {
	if tram([][2]int{{0, 3}, {2, 5}, {4, 2}, {4, 0}}) != 6 {
		panic("tram failed")
	}
	fmt.Println("116A tram ok")
}
