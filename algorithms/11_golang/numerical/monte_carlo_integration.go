package main

import (
	"fmt"
	"math"
)

func monteCarloIntegration(f func(float64) float64, a, b float64, samples int) float64 {
	state := int64(42)
	modulus := int64(1) << 31
	total := 0.0
	for i := 0; i < samples; i++ {
		state = (1103515245*state + 12345) % modulus
		total += f(a + (b-a)*float64(state)/float64(modulus))
	}
	return (b - a) * total / float64(samples)
}

func main() {
	estimate := monteCarloIntegration(func(x float64) float64 { return x * x }, 0, 1, 100000)
	if math.Abs(estimate-1.0/3.0) > 0.01 {
		panic("monte carlo failed")
	}
	fmt.Println("monte carlo integration ok")
}
