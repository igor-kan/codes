package main

import "fmt"

func wrongSubtraction(number int64, steps int) int64 {
	for i := 0; i < steps; i++ {
		if number%10 == 0 {
			number /= 10
		} else {
			number--
		}
	}
	return number
}

func main() {
	if wrongSubtraction(512, 4) != 50 || wrongSubtraction(1000000000, 9) != 1 {
		panic("wrong subtraction failed")
	}
	fmt.Println("977A wrong subtraction ok")
}
