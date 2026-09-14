package main

import "fmt"

func minInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type SparseTable struct {
	st  [][]int
	log []int
}

func NewSparseTable(arr []int) *SparseTable {
	n := len(arr)
	log := make([]int, n+1)
	for i := 2; i <= n; i++ {
		log[i] = log[i/2] + 1
	}
	k := log[n] + 1
	st := make([][]int, n)
	for i := 0; i < n; i++ {
		st[i] = make([]int, k)
		st[i][0] = arr[i]
	}
	for j := 1; j < k; j++ {
		for i := 0; i+(1<<j) <= n; i++ {
			st[i][j] = minInt(st[i][j-1], st[i+(1<<(j-1))][j-1])
		}
	}
	return &SparseTable{st: st, log: log}
}

func (s *SparseTable) Query(l, r int) int {
	j := s.log[r-l+1]
	return minInt(s.st[l][j], s.st[r-(1<<j)+1][j])
}

func main() {
	arr := []int{2, 5, 1, 4, 9, 3}
	st := NewSparseTable(arr)
	if st.Query(0, 5) != 1 || st.Query(1, 3) != 1 || st.Query(4, 5) != 3 || st.Query(0, 0) != 2 {
		panic("SparseTable: RMQ mismatch")
	}
	fmt.Println("[Go SparseTable] Range minimum query verified.")
}
