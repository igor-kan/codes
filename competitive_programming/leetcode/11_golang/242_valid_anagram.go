package main

import (
	"fmt"
	"strings"
	"sort"
)

func validAnagram(s, t string) bool {
	left := strings.Split(s, "")
	right := strings.Split(t, "")
	sort.Strings(left)
	sort.Strings(right)
	return strings.Join(left, "") == strings.Join(right, "")
}

func main() {
	if !validAnagram("anagram", "nagaram") || validAnagram("rat", "car") {
		panic("valid anagram failed")
	}
	fmt.Println("242 valid anagram ok")
}
