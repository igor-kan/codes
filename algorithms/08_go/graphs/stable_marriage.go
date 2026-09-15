package main

import "fmt"

func main() {
	menPref := [][]int{{0, 1, 2}, {1, 0, 2}, {0, 1, 2}}
	womenPref := [][]int{{2, 1, 0}, {0, 1, 2}, {0, 1, 2}}
	n := 3
	rank := make([][]int, n)
	for w := 0; w < n; w++ {
		rank[w] = make([]int, n)
		for i, m := range womenPref[w] {
			rank[w][m] = i
		}
	}
	free := []int{0, 1, 2}
	next := make([]int, n)
	engagedTo := []int{-1, -1, -1}
	for len(free) > 0 {
		m := free[len(free)-1]
		free = free[:len(free)-1]
		w := menPref[m][next[m]]
		next[m]++
		if engagedTo[w] == -1 {
			engagedTo[w] = m
		} else if rank[w][m] < rank[w][engagedTo[w]] {
			free = append(free, engagedTo[w])
			engagedTo[w] = m
		} else {
			free = append(free, m)
		}
	}
	want := []int{2, 0, 1}
	for i := range want {
		if engagedTo[i] != want[i] {
			panic("stable marriage mismatch")
		}
	}
	fmt.Println("stable marriage ok")
}
