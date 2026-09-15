package main

import "fmt"

func nearlyLuckyNumber(number int64) string {
	count := 0
	for _, digit := range fmt.Sprintf("%d", number) {
		if digit == '4' || digit == '7' {
			count++
		}
	}
	if count == 4 || count == 7 {
		return "YES"
	}
	return "NO"
}

func main() {
	if nearlyLuckyNumber(47) != "NO" || nearlyLuckyNumber(7747774) != "YES" || nearlyLuckyNumber(40047) != "NO" {
		panic("nearly lucky failed")
	}
	fmt.Println("110A nearly lucky number ok")
}
