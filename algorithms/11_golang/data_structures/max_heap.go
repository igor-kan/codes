// Binary max-heap via container/heap.
package main

import (
	"container/heap"
	"fmt"
)

type maxHeap []int

func (h maxHeap) Len() int           { return len(h) }
func (h maxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *maxHeap) Pop() any {
	old := *h
	n := len(old)
	v := old[n-1]
	*h = old[:n-1]
	return v
}

func main() {
	h := &maxHeap{5, 3, 8, 1, 4}
	heap.Init(h)
	prev := 1 << 30
	for h.Len() > 0 {
		x := heap.Pop(h).(int)
		if x > prev {
			panic("not a max-heap order")
		}
		prev = x
	}
	fmt.Println("max heap ok")
}
