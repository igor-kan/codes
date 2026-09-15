package main

import (
	"fmt"
	"math"
)

func aitken(x0, x1, x2 float64) float64 {
	denominator := x2 - 2*x1 + x0
	if math.Abs(denominator) < 1e-15 {
		return x2
	}
	return x2 - (x2-x1)*(x2-x1)/denominator
}

func main() {
	if math.Abs(aitken(1, 0.5, 0.25)) > 1e-12 {
		panic("aitken geometric failed")
	}
	sequence := make([]float64, 3)
	for n := 0; n < 3; n++ {
		sequence[n] = 2 - 2*math.Pow(0.5, float64(n))
	}
	if math.Abs(aitken(sequence[0], sequence[1], sequence[2])-2) > 1e-12 {
		panic("aitken failed")
	}
	fmt.Println("aitken ok")
}
