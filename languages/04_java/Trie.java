/**
 * Prefix Tree (Trie) with Autocomplete and Search.
 * 
 * Why Java for this module?
 * Java's robust object model, Garbage Collection, and Unicode UTF-16 character
 * handling make it the foundation for enterprise search engines (Elasticsearch, Apache Lucene).
 */

import java.util.*;

public class Trie {
    private static class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        boolean isEndOfWord = false;
    }

    private final TrieNode root;

    public Trie() {
        this.root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode curr = root;
        for (char ch : word.toCharArray()) {
            curr.children.putIfAbsent(ch, new TrieNode());
            curr = curr.children.get(ch);
        }
        curr.isEndOfWord = true;
    }

    public boolean search(String word) {
        TrieNode node = findNode(word);
        return node != null && node.isEndOfWord;
    }

    public boolean startsWith(String prefix) {
        return findNode(prefix) != null;
    }

    public List<String> autocomplete(String prefix) {
        List<String> results = new ArrayList<>();
        TrieNode prefixNode = findNode(prefix);
        if (prefixNode != null) {
            dfsCollect(prefixNode, new StringBuilder(prefix), results);
        }
        return results;
    }

    private TrieNode findNode(String str) {
        TrieNode curr = root;
        for (char ch : str.toCharArray()) {
            curr = curr.children.get(ch);
            if (curr == null) return null;
        }
        return curr;
    }

    private void dfsCollect(TrieNode node, StringBuilder currentWord, List<String> results) {
        if (node.isEndOfWord) {
            results.add(currentWord.toString());
        }
        for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
            currentWord.append(entry.getKey());
            dfsCollect(entry.getValue(), currentWord, results);
            currentWord.deleteCharAt(currentWord.length() - 1);
        }
    }

    public static void main(String[] args) {
        Trie trie = new Trie();
        trie.insert("quarto");
        trie.insert("quantum");
        trie.insert("quadratic");
        trie.insert("quasar");

        System.out.println("Java Trie Autocomplete for prefix "qua": " + trie.autocomplete("qua"));
        assert trie.search("quantum");
        assert !trie.search("quiver");
        System.out.println("Trie verification completed successfully.");
    }
}
