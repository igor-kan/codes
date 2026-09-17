// Package data_structures implements Skip List in Go.
package data_structures

import "math/rand"

type SkipNode struct {
	Value   int
	Forward []*SkipNode
}

type SkipList struct {
	header *SkipNode
	level  int
}

func NewSkipList() *SkipList {
	return &SkipList{
		header: &SkipNode{Forward: make([]*SkipNode, 16)},
		level:  0,
	}
}

func (sl *SkipList) Insert(val int) {
	update := make([]*SkipNode, 16)
	curr := sl.header
	for i := sl.level; i >= 0; i-- {
		for curr.Forward[i] != nil && curr.Forward[i].Value < val {
			curr = curr.Forward[i]
		}
		update[i] = curr
	}
	lvl := 0
	for rand.Float64() < 0.5 && lvl < 15 {
		lvl++
	}
	newNode := &SkipNode{Value: val, Forward: make([]*SkipNode, lvl+1)}
	for i := 0; i <= lvl; i++ {
		newNode.Forward[i] = update[i].Forward[i]
		update[i].Forward[i] = newNode
	}
}

func (sl *SkipList) Search(val int) bool {
	curr := sl.header
	for i := sl.level; i >= 0; i-- {
		for curr.Forward[i] != nil && curr.Forward[i].Value < val {
			curr = curr.Forward[i]
		}
	}
	curr = curr.Forward[0]
	return curr != nil && curr.Value == val
}
