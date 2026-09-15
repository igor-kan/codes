package main

import "fmt"

func theatreSquare(n, m, a int64) int64 {
	return ((n + a - 1) / a) * ((m + a - 1) / a)
}

func main() {
	if theatreSquare(6, 6, 4) != 4 || theatreSquare(1, 1, 1) != 1 {
		panic("theatre square failed")
	}
	fmt.Println("1A theatre square ok")
}
