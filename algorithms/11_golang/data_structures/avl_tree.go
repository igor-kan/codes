// Self-balancing AVL tree.
package main

import "fmt"

type node struct {
	key, height  int
	left, right  *node
}

func height(n *node) int {
	if n == nil {
		return 0
	}
	return n.height
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func update(n *node) { n.height = 1 + max(height(n.left), height(n.right)) }

func rotateRight(y *node) *node {
	x := y.left
	y.left = x.right
	x.right = y
	update(y)
	update(x)
	return x
}

func rotateLeft(x *node) *node {
	y := x.right
	x.right = y.left
	y.left = x
	update(x)
	update(y)
	return y
}

func balance(n *node) *node {
	update(n)
	factor := height(n.left) - height(n.right)
	if factor > 1 {
		if height(n.left.left) < height(n.left.right) {
			n.left = rotateLeft(n.left)
		}
		return rotateRight(n)
	}
	if factor < -1 {
		if height(n.right.right) < height(n.right.left) {
			n.right = rotateRight(n.right)
		}
		return rotateLeft(n)
	}
	return n
}

func insert(n *node, key int) *node {
	if n == nil {
		return &node{key: key, height: 1}
	}
	if key < n.key {
		n.left = insert(n.left, key)
	} else if key > n.key {
		n.right = insert(n.right, key)
	} else {
		return n
	}
	return balance(n)
}

func inorder(n *node, out *[]int) {
	if n == nil {
		return
	}
	inorder(n.left, out)
	*out = append(*out, n.key)
	inorder(n.right, out)
}

func main() {
	var root *node
	for _, key := range []int{10, 20, 30, 40, 50, 25} {
		root = insert(root, key)
	}
	var out []int
	inorder(root, &out)
	for i := 1; i < len(out); i++ {
		if out[i-1] > out[i] {
			panic("not sorted")
		}
	}
	fmt.Println("avl tree ok")
}
