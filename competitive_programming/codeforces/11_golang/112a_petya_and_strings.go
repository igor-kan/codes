package main

import (
	"fmt"
	"strings"
)

func petyaAndStrings(a, b string) int {
	left, right := strings.ToLower(a), strings.ToLower(b)
	if left < right {
		return -1
	}
	if left > right {
		return 1
	}
	return 0
}

func main() {
	if petyaAndStrings("aaaa", "aaaA") != 0 || petyaAndStrings("abs", "Abz") != -1 || petyaAndStrings("abcdefg", "AbCdEfF") != 1 {
		panic("petya failed")
	}
	fmt.Println("112A petya and strings ok")
}
