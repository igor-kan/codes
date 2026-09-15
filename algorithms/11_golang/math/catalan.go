// Catalan numbers by the recurrence.
package main

import "fmt"

func main() {
	c := make([]int64, 11)
	c[0] = 1
	for i := 1; i <= 10; i++ {
		var sum int64
		for j := 0; j < i; j++ {
			sum += c[j] * c[i-1-j]
		}
		c[i] = sum
	}
	if c[5] != 42 || c[10] != 16796 {
		panic("wrong Catalan numbers")
	}
	fmt.Println("catalan(10)=", c[10])
}
