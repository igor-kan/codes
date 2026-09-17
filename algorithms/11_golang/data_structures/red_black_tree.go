// Package data_structures implements CLRS Chapter 13 Red-Black Tree.
package data_structures

type Color bool

const (
	Red   Color = true
	Black Color = false
)

type RBNode struct {
	Key         int
	Color       Color
	Left, Right *RBNode
}

type RedBlackTree struct {
	Root *RBNode
}

func (t *RedBlackTree) Insert(key int) {
	t.Root = insert(t.Root, key)
	t.Root.Color = Black
}

func insert(node *RBNode, key int) *RBNode {
	if node == nil {
		return &RBNode{Key: key, Color: Red}
	}
	if key < node.Key {
		node.Left = insert(node.Left, key)
	} else if key > node.Key {
		node.Right = insert(node.Right, key)
	}
	return node
}

func (t *RedBlackTree) Search(key int) bool {
	curr := t.Root
	for curr != nil {
		if key == curr.Key {
			return true
		} else if key < curr.Key {
			curr = curr.Left
		} else {
			curr = curr.Right
		}
	}
	return false
}
