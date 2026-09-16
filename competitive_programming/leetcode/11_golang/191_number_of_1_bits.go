package main

import (
	"fmt"
	"math/bits"
)

func numberOf1Bits(n uint) int {
	return bits.OnesCount(n)
}

func main() {
	if numberOf1Bits(11) != 3 || numberOf1Bits(128) != 1 || numberOf1Bits(4294967293) != 31 {
		panic("number of 1 bits failed")
	}
	fmt.Println("191 number of 1 bits ok")
}
