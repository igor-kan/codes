package main

import (
	"fmt"
	"strings"
)

func strStr(haystack, needle string) int {
	return strings.Index(haystack, needle)
}

func main() {
	if strStr("sadbutsad", "sad") != 0 || strStr("leetcode", "leeto") != -1 {
		panic("strStr failed")
	}
	fmt.Println("28 find index first occurrence ok")
}
