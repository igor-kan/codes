package main

import "fmt"

func palindromeNumber(x int) bool {
	if x < 0 {
		return false
	}
	digits := fmt.Sprintf("%d", x)
	for i, j := 0, len(digits)-1; i < j; i, j = i+1, j-1 {
		if digits[i] != digits[j] {
			return false
		}
	}
	return true
}

func main() {
	if !palindromeNumber(121) || palindromeNumber(-121) || palindromeNumber(10) {
		panic("palindrome number failed")
	}
	fmt.Println("9 palindrome number ok")
}
