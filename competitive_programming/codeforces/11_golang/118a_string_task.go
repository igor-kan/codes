package main

import (
	"fmt"
	"strings"
)

func stringTask(text string) string {
	vowels := "aeiouy"
	var builder strings.Builder
	for _, character := range strings.ToLower(text) {
		if !strings.ContainsRune(vowels, character) {
			builder.WriteByte('.')
			builder.WriteRune(character)
		}
	}
	return builder.String()
}

func main() {
	if stringTask("Codeforces") != ".c.d.f.r.c.s" || stringTask("aBAcAba") != ".b.c.b" {
		panic("string task failed")
	}
	fmt.Println("118A string task ok")
}
