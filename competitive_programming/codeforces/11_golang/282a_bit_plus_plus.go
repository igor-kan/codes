package main

import (
	"fmt"
	"strings"
)

func bitPlusPlus(operations []string) int {
	value := 0
	for _, operation := range operations {
		if strings.Contains(operation, "++") {
			value++
		} else {
			value--
		}
	}
	return value
}

func main() {
	if bitPlusPlus([]string{"++X", "X++", "--X"}) != 1 || bitPlusPlus([]string{"X++", "X++", "X++", "X--"}) != 2 {
		panic("bit++ failed")
	}
	fmt.Println("282A bit++ ok")
}
