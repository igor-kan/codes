package main

import "fmt"

type DSU struct {
	parent []int
	size   []int
}

func NewDSU(n int) *DSU {
	parent := make([]int, n)
	size := make([]int, n)
	for i := 0; i < n; i++ {
		parent[i] = i
		size[i] = 1
	}
	return &DSU{parent: parent, size: size}
}

func (d *DSU) Find(x int) int {
	if d.parent[x] != x {
		d.parent[x] = d.Find(d.parent[x])
	}
	return d.parent[x]
}

func (d *DSU) Union(a, b int) bool {
	ra, rb := d.Find(a), d.Find(b)
	if ra == rb {
		return false
	}
	if d.size[ra] < d.size[rb] {
		ra, rb = rb, ra
	}
	d.parent[rb] = ra
	d.size[ra] += d.size[rb]
	return true
}

func main() {
	d := NewDSU(6)
	d.Union(0, 1)
	d.Union(1, 2)
	d.Union(3, 4)
	if d.Find(0) != d.Find(2) {
		panic("DSU: 0 and 2 should be connected")
	}
	if d.Find(0) == d.Find(3) {
		panic("DSU: 0 and 3 should be separate")
	}
	if d.size[d.Find(0)] != 3 {
		panic("DSU: component size should be 3")
	}
	fmt.Println("[Go DSU] Path compression + union by size verified.")
}
