package main

import (
	"fmt"
	"strings"
	"sort"
)

func helpfulMaths(expression string) string {
	parts := strings.Split(expression, "+")
	sort.Strings(parts)
	return strings.Join(parts, "+")
}

func main() {
	if helpfulMaths("3+2+1") != "1+2+3" || helpfulMaths("1+1+3+1+3") != "1+1+1+3+3" {
		panic("helpful maths failed")
	}
	fmt.Println("339A helpful maths ok")
}
