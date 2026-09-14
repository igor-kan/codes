package main

import (
	"fmt"
	"reflect"
)

func computeLPS(pattern string) []int {
	m := len(pattern)
	lps := make([]int, m)
	length := 0
	i := 1

	for i < m {
		if pattern[i] == pattern[length] {
			length++
			lps[i] = length
			i++
		} else {
			if length != 0 {
				length = lps[length-1]
			} else {
				lps[i] = 0
				i++
			}
		}
	}
	return lps
}

func KMPSearch(text, pattern string) []int {
	n, m := len(text), len(pattern)
	if m == 0 || n == 0 {
		return nil
	}

	lps := computeLPS(pattern)
	var occurrences []int

	i, j := 0, 0
	for i < n {
		if text[i] == pattern[j] {
			i++
			j++
		}

		if j == m {
			occurrences = append(occurrences, i-j)
			j = lps[j-1]
		} else if i < n && text[i] != pattern[j] {
			if j != 0 {
				j = lps[j-1]
			} else {
				i++
			}
		}
	}

	return occurrences
}

func main() {
	txt := "ABABDABACDABABCABABABABCABAB"
	pat := "ABABCABAB"
	matches := KMPSearch(txt, pat)

	expected := []int{10, 19}
	if !reflect.DeepEqual(matches, expected) {
		panic(fmt.Sprintf("Expected %v, got %v", expected, matches))
	}

	fmt.Printf("[Go KMP] Matches confirmed at indices: %v\n", matches)
}
