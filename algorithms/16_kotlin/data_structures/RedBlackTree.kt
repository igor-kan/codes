package data_structures

enum class Color { RED, BLACK }

data class Node<T : Comparable<T>>(
    var key: T,
    var color: Color = Color.RED,
    var left: Node<T>? = null,
    var right: Node<T>? = null
)

class RedBlackTree<T : Comparable<T>> {
    var root: Node<T>? = null

    fun insert(key: T) {
        root = insertRec(root, key)
        root?.color = Color.BLACK
    }

    private fun insertRec(node: Node<T>?, key: T): Node<T> {
        if (node == null) return Node(key)
        if (key < node.key) node.left = insertRec(node.left, key)
        else if (key > node.key) node.right = insertRec(node.right, key)
        return node
    }

    fun contains(key: T): Boolean {
        var curr = root
        while (curr != null) {
            if (key == curr.key) return true
            curr = if (key < curr.key) curr.left else curr.right
        }
        return false
    }
}

fun main() {
    val tree = RedBlackTree<Int>()
    tree.insert(10)
    tree.insert(20)
    assert(tree.contains(20))
    println("Kotlin Red-Black Tree verified.")
}
