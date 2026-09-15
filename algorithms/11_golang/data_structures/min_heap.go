// Binary min-heap built on container/heap.
package main

import (
	"container/heap"
	"fmt"
)

type intHeap []int

func (h intHeap) Len() int            { return len(h) }
func (h intHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h intHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *intHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *intHeap) Pop() interface{} {
	old := *h
	n := len(old)
	value := old[n-1]
	*h = old[:n-1]
	return value
}

func main() {
	h := &intHeap{5, 3, 8, 1, 4}
	heap.Init(h)
	previous := -1
	for h.Len() > 0 {
		value := heap.Pop(h).(int)
		if value < previous {
			panic("not sorted")
		}
		previous = value
	}
	fmt.Println("min heap ok")
}
