package main

import "fmt"

func stonesOnTable(row string) int {
	removals := 0
	for i := 1; i < len(row); i++ {
		if row[i] == row[i-1] {
			removals++
		}
	}
	return removals
}

func main() {
	if stonesOnTable("RRG") != 1 || stonesOnTable("RRRRR") != 4 || stonesOnTable("BRBG") != 0 {
		panic("stones failed")
	}
	fmt.Println("266A stones on the table ok")
}
