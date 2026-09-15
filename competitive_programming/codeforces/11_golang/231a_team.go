package main

import "fmt"

func team(problems [][3]int) int {
	count := 0
	for _, p := range problems {
		if p[0]+p[1]+p[2] >= 2 {
			count++
		}
	}
	return count
}

func main() {
	if team([][3]int{{1, 1, 0}, {1, 1, 1}, {1, 0, 0}}) != 2 {
		panic("team failed")
	}
	fmt.Println("231A team ok")
}
