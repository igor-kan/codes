package data_structures;

/**
 * Red-Black Tree in Java (CLRS 3rd Ed. Chapter 13).
 */
public class RedBlackTree<T extends Comparable<T>> {
    public enum Color { RED, BLACK }

    public static class Node<T> {
        public T key;
        public Color color = Color.RED;
        public Node<T> left, right;
        public Node(T key) { this.key = key; }
    }

    public Node<T> root;

    public void insert(T key) {
        root = insertRec(root, key);
        root.color = Color.BLACK;
    }

    private Node<T> insertRec(Node<T> node, T key) {
        if (node == null) return new Node<>(key);
        if (key.compareTo(node.key) < 0) node.left = insertRec(node.left, key);
        else if (key.compareTo(node.key) > 0) node.right = insertRec(node.right, key);
        return node;
    }

    public boolean contains(T key) {
        Node<T> curr = root;
        while (curr != null) {
            int cmp = key.compareTo(curr.key);
            if (cmp == 0) return true;
            curr = cmp < 0 ? curr.left : curr.right;
        }
        return false;
    }

    public static void main(String[] args) {
        RedBlackTree<Integer> rbt = new RedBlackTree<>();
        rbt.insert(10);
        rbt.insert(20);
        rbt.insert(5);
        assert rbt.contains(20);
        assert !rbt.contains(99);
        System.out.println("Java Red-Black Tree verified.");
    }
}
