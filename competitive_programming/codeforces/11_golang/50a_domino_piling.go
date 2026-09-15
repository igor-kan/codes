package main

import "fmt"

func dominoPiling(m, n int) int {
	return m * n / 2
}

func main() {
	if dominoPiling(2, 4) != 4 || dominoPiling(3, 3) != 4 {
		panic("domino piling failed")
	}
	fmt.Println("50A domino piling ok")
}
