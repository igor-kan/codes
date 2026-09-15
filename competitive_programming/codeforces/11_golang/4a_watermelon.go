package main

import "fmt"

func watermelon(weight int) string {
	if weight%2 == 0 && weight > 2 {
		return "YES"
	}
	return "NO"
}

func main() {
	if watermelon(8) != "YES" || watermelon(2) != "NO" || watermelon(3) != "NO" {
		panic("watermelon failed")
	}
	fmt.Println("4A watermelon ok")
}
