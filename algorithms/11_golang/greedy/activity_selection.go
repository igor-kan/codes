package main

import (
	"fmt"
	"sort"
)

type activity struct{ start, finish int }

func main() {
	acts := []activity{{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 9}, {5, 9},
		{6, 10}, {8, 11}, {8, 12}, {2, 14}, {12, 16}}
	sort.Slice(acts, func(i, j int) bool { return acts[i].finish < acts[j].finish })
	var chosen [][2]int
	last := -1
	for _, a := range acts {
		if a.start >= last {
			chosen = append(chosen, [2]int{a.start, a.finish})
			last = a.finish
		}
	}
	want := [][2]int{{1, 4}, {5, 7}, {8, 11}, {12, 16}}
	if len(chosen) != len(want) {
		panic("activity selection mismatch")
	}
	for i := range want {
		if chosen[i] != want[i] {
			panic("activity selection mismatch")
		}
	}
	fmt.Println("activity selection ok")
}
