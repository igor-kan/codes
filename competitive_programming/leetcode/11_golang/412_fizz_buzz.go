package main

import "fmt"

func fizzBuzz(n int) []string {
	result := []string{}
	for value := 1; value <= n; value++ {
		switch {
		case value%15 == 0:
			result = append(result, "FizzBuzz")
		case value%3 == 0:
			result = append(result, "Fizz")
		case value%5 == 0:
			result = append(result, "Buzz")
		default:
			result = append(result, fmt.Sprintf("%d", value))
		}
	}
	return result
}

func main() {
	if fmt.Sprint(fizzBuzz(5)) != "[1 2 Fizz 4 Buzz]" || fizzBuzz(15)[14] != "FizzBuzz" {
		panic("fizz buzz failed")
	}
	fmt.Println("412 fizz buzz ok")
}
