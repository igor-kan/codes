final class Trie {
    private final class Node {
        var children: [Character: Node] = [:]
        var isEnd = false
    }
    private let root = Node()

    func insert(_ word: String) {
        var node = root
        for c in word { node = node.children[c, default: Node()] }
        node.isEnd = true
    }
    func search(_ word: String) -> Bool {
        var node = root
        for c in word { guard let next = node.children[c] else { return false }; node = next }
        return node.isEnd
    }
    func starts(with prefix: String) -> Bool {
        var node = root
        for c in prefix { guard let next = node.children[c] else { return false }; node = next }
        return true
    }
}
print("[Swift Trie] Testing Trie data structure")
let trie = Trie()
trie.insert("apple")
print("search apple: \(trie.search("apple")) (expected true)")
print("search app: \(trie.search("app")) (expected false)")
print("startsWith app: \(trie.starts(with: "app")) (expected true)")
trie.insert("app")
print("search app: \(trie.search("app")) (expected true)")
print("[Swift Trie] Test completed.")