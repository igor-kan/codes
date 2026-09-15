package main

import "fmt"

func beautifulMatrix(grid [5][5]int) int {
	for row := 0; row < 5; row++ {
		for column := 0; column < 5; column++ {
			if grid[row][column] == 1 {
				return abs(row-2) + abs(column-2)
			}
		}
	}
	return -1
}

func abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}

func main() {
	grid := [5][5]int{{0, 0, 0, 0, 0}, {0, 0, 0, 0, 1}, {0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}}
	if beautifulMatrix(grid) != 3 {
		panic("beautiful matrix failed")
	}
	fmt.Println("263A beautiful matrix ok")
}
