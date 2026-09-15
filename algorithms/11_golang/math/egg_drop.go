// Egg dropping: minimum trials with k eggs and n floors.
package main

import "fmt"

func main() {
	eggs, floors := 2, 100
	dp := make([][]int, 101)
	for i := range dp {
		dp[i] = make([]int, eggs+1)
	}
	t := 0
	for dp[t][eggs] < floors {
		t++
		for k := 1; k <= eggs; k++ {
			dp[t][k] = dp[t-1][k-1] + dp[t-1][k] + 1
		}
	}
	if t != 14 {
		panic("expected 14 trials")
	}
	fmt.Println("egg drop=", t)
}
