package main

import "fmt"

type LazySegTree struct {
	tree []int
	lazy []int
	n    int
}

func NewLazySegTree(arr []int) *LazySegTree {
	n := len(arr)
	tree := make([]int, 4*n)
	lazy := make([]int, 4*n)
	st := &LazySegTree{tree: tree, lazy: lazy, n: n}
	if n > 0 {
		st.build(1, 0, n-1, arr)
	}
	return st
}

func (s *LazySegTree) build(node, lo, hi int, arr []int) {
	if lo == hi {
		s.tree[node] = arr[lo]
		return
	}
	mid := (lo + hi) / 2
	s.build(node*2, lo, mid, arr)
	s.build(node*2+1, mid+1, hi, arr)
	s.tree[node] = s.tree[node*2] + s.tree[node*2+1]
}

func (s *LazySegTree) push(node, lo, hi int) {
	if s.lazy[node] != 0 {
		s.tree[node] += (hi - lo + 1) * s.lazy[node]
		if lo != hi {
			s.lazy[node*2] += s.lazy[node]
			s.lazy[node*2+1] += s.lazy[node]
		}
		s.lazy[node] = 0
	}
}

func (s *LazySegTree) Update(l, r, val int) { s.update(1, 0, s.n-1, l, r, val) }

func (s *LazySegTree) update(node, lo, hi, l, r, val int) {
	s.push(node, lo, hi)
	if r < lo || hi < l {
		return
	}
	if l <= lo && hi <= r {
		s.lazy[node] += val
		s.push(node, lo, hi)
		return
	}
	mid := (lo + hi) / 2
	s.update(node*2, lo, mid, l, r, val)
	s.update(node*2+1, mid+1, hi, l, r, val)
	s.tree[node] = s.tree[node*2] + s.tree[node*2+1]
}

func (s *LazySegTree) Query(l, r int) int { return s.query(1, 0, s.n-1, l, r) }

func (s *LazySegTree) query(node, lo, hi, l, r int) int {
	s.push(node, lo, hi)
	if r < lo || hi < l {
		return 0
	}
	if l <= lo && hi <= r {
		return s.tree[node]
	}
	mid := (lo + hi) / 2
	return s.query(node*2, lo, mid, l, r) + s.query(node*2+1, mid+1, hi, l, r)
}

func main() {
	arr := []int{1, 2, 3, 4, 5}
	st := NewLazySegTree(arr)
	if st.Query(0, 4) != 15 {
		panic("LazySegTree: initial sum should be 15")
	}
	st.Update(1, 3, 2) // [1,4,5,6,5]
	if st.Query(0, 4) != 21 || st.Query(1, 3) != 15 || st.Query(2, 2) != 5 {
		panic("LazySegTree: update/query mismatch")
	}
	fmt.Println("[Go LazySegTree] Range add / range sum verified.")
}
