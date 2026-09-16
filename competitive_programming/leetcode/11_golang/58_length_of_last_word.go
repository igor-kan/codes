package main

import (
	"fmt"
	"strings"
)

func lengthOfLastWord(text string) int {
	words := strings.Fields(text)
	if len(words) == 0 {
		return 0
	}
	return len(words[len(words)-1])
}

func main() {
	if lengthOfLastWord("Hello World") != 5 || lengthOfLastWord("   fly me   to   the moon  ") != 4 {
		panic("length of last word failed")
	}
	fmt.Println("58 length of last word ok")
}
