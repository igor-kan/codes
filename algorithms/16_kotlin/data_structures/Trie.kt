class Trie {
    private class Node {
        val children = HashMap<Char, Node>()
        var isEnd = false
    }
    private val root = Node()

    fun insert(word: String) {
        var node = root
        for (c in word) node = node.children.getOrPut(c) { Node() }
        node.isEnd = true
    }
    fun search(word: String): Boolean {
        var node = root
        for (c in word) { node = node.children[c] ?: return false }
        return node.isEnd
    }
    fun startsWith(prefix: String): Boolean {
        var node = root
        for (c in prefix) { node = node.children[c] ?: return false }
        return true
    }
}
fun main() {
    println("[Kotlin Trie] Testing Trie data structure")
    val trie = Trie()
    trie.insert("apple")
    println("search apple: ${trie.search("apple")} (expected true)")
    println("search app: ${trie.search("app")} (expected false)")
    println("startsWith app: ${trie.startsWith("app")} (expected true)")
    trie.insert("app")
    println("search app: ${trie.search("app")} (expected true)")
    println("[Kotlin Trie] Test completed.")
}