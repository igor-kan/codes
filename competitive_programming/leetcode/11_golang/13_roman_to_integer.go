package main

import "fmt"

var romanValues = map[byte]int{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

func romanToInteger(text string) int {
	total := 0
	for i := 0; i < len(text); i++ {
		value := romanValues[text[i]]
		if i+1 < len(text) && value < romanValues[text[i+1]] {
			total -= value
		} else {
			total += value
		}
	}
	return total
}

func main() {
	if romanToInteger("III") != 3 || romanToInteger("LVIII") != 58 || romanToInteger("MCMXCIV") != 1994 {
		panic("roman to integer failed")
	}
	fmt.Println("13 roman to integer ok")
}
