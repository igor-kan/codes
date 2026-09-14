package main

import "fmt"

func manacher(s string) string {
	t := []byte{'#'}
	for i := 0; i < len(s); i++ {
		t = append(t, s[i], '#')
	}
	n := len(t)
	p := make([]int, n)
	c, r := 0, 0
	for i := 0; i < n; i++ {
		mirror := 2*c - i
		if i < r {
			if p[mirror] < r-i {
				p[i] = p[mirror]
			} else {
				p[i] = r - i
			}
		}
		for i-p[i]-1 >= 0 && i+p[i]+1 < n && t[i-p[i]-1] == t[i+p[i]+1] {
			p[i]++
		}
		if i+p[i] > r {
			c, r = i, i+p[i]
		}
	}
	center, maxLen := 0, 0
	for i := 0; i < n; i++ {
		if p[i] > maxLen {
			maxLen = p[i]
			center = i
		}
	}
	start := (center - maxLen) / 2
	return s[start : start+maxLen]
}

func main() {
	if manacher("babad") != "bab" && manacher("babad") != "aba" {
		panic("Manacher: longest palindrome for 'babad' should be 'bab' or 'aba'")
	}
	if manacher("cbbd") != "bb" {
		panic("Manacher: longest palindrome for 'cbbd' should be 'bb'")
	}
	if manacher("racecar") != "racecar" {
		panic("Manacher: full palindrome failed")
	}
	fmt.Println("[Go Manacher] Longest palindromic substring verified.")
}
