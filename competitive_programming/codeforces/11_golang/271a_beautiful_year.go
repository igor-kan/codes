package main

import "fmt"

func beautifulYear(year int) int {
	for {
		year++
		digits := map[rune]bool{}
		for _, digit := range fmt.Sprintf("%d", year) {
			digits[digit] = true
		}
		if len(digits) == 4 {
			return year
		}
	}
}

func main() {
	if beautifulYear(1987) != 2013 || beautifulYear(2013) != 2014 {
		panic("beautiful year failed")
	}
	fmt.Println("271A beautiful year ok")
}
