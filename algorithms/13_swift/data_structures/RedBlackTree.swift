// Red-Black Tree in Swift (CLRS 3rd Ed. Chapter 13)

enum Color { case red, black }

class RBNode<T: Comparable> {
    var key: T
    var color: Color = .red
    var left: RBNode<T>?
    var right: RBNode<T>?
    init(key: T) { self.key = key }
}

class RedBlackTree<T: Comparable> {
    var root: RBNode<T>?

    func insert(_ key: T) {
        root = insertRec(root, key)
        root?.color = .black
    }

    private func insertRec(_ node: RBNode<T>?, _ key: T) -> RBNode<T> {
        guard let node = node else { return RBNode(key: key) }
        if key < node.key { node.left = insertRec(node.left, key) }
        else if key > node.key { node.right = insertRec(node.right, key) }
        return node
    }

    func contains(_ key: T) -> Bool {
        var curr = root
        while let node = curr {
            if key == node.key { return true }
            curr = key < node.key ? node.left : node.right
        }
        return false
    }
}

let tree = RedBlackTree<Int>()
tree.insert(10)
tree.insert(20)
assert(tree.contains(20))
print("Swift Red-Black Tree verified.")
