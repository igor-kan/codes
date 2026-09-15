package main

import "fmt"

func soldierAndBananas(cost, money, count int64) int64 {
	total := cost * count * (count + 1) / 2
	if total > money {
		return total - money
	}
	return 0
}

func main() {
	if soldierAndBananas(3, 17, 4) != 13 || soldierAndBananas(1, 100, 1) != 0 {
		panic("soldier and bananas failed")
	}
	fmt.Println("546A soldier and bananas ok")
}
