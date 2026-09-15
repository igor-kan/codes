// Fixed-size circular buffer.
package main

import "fmt"

type circularBuffer struct {
	data []int
	head int
	size int
}

func newCircularBuffer(capacity int) *circularBuffer {
	return &circularBuffer{data: make([]int, capacity)}
}

func (b *circularBuffer) push(v int) {
	n := len(b.data)
	b.data[(b.head+b.size)%n] = v
	if b.size < n {
		b.size++
	} else {
		b.head = (b.head + 1) % n
	}
}

func (b *circularBuffer) pop() int {
	v := b.data[b.head]
	b.head = (b.head + 1) % len(b.data)
	b.size--
	return v
}

func main() {
	b := newCircularBuffer(3)
	for i := 1; i <= 4; i++ {
		b.push(i)
	}
	if b.pop() != 2 || b.pop() != 3 || b.pop() != 4 {
		panic("bad overwrite semantics")
	}
	fmt.Println("circular buffer ok")
}
