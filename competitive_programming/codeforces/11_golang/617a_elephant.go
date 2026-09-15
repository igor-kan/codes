package main

import "fmt"

func elephant(position int) int {
	return (position + 4) / 5
}

func main() {
	if elephant(5) != 1 || elephant(12) != 3 || elephant(1) != 1 {
		panic("elephant failed")
	}
	fmt.Println("617A elephant ok")
}
