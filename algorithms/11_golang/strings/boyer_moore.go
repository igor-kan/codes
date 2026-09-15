// Boyer-Moore-Horspool substring search.
package main

import "fmt"

func boyerMoore(text, pat string) int {
	n, m := len(text), len(pat)
	skip := [256]int{}
	for i := range skip {
		skip[i] = m
	}
	for i := 0; i < m-1; i++ {
		skip[pat[i]] = m - 1 - i
	}
	i := 0
	for i+m <= n {
		j := m - 1
		for j >= 0 && text[i+j] == pat[j] {
			j--
		}
		if j < 0 {
			return i
		}
		i += skip[text[i+m-1]]
	}
	return -1
}

func main() {
	if boyerMoore("here is a simple example", "example") != 17 || boyerMoore("abc", "xyz") != -1 {
		panic("search failed")
	}
	fmt.Println("boyer-moore ok")
}
