import java.util.ArrayList;
import java.util.List;

public final class AVLTree {
    private static final class Node {
        int key;
        int height = 1;
        Node left;
        Node right;

        Node(int key) {
            this.key = key;
        }
    }

    private Node root;

    private static int height(Node node) {
        return node == null ? 0 : node.height;
    }

    private static void update(Node node) {
        node.height = 1 + Math.max(height(node.left), height(node.right));
    }

    private static Node rotateRight(Node y) {
        Node x = y.left;
        y.left = x.right;
        x.right = y;
        update(y);
        update(x);
        return x;
    }

    private static Node rotateLeft(Node x) {
        Node y = x.right;
        x.right = y.left;
        y.left = x;
        update(x);
        update(y);
        return y;
    }

    private static Node balance(Node node) {
        update(node);
        int factor = height(node.left) - height(node.right);
        if (factor > 1) {
            if (height(node.left.left) < height(node.left.right)) {
                node.left = rotateLeft(node.left);
            }
            return rotateRight(node);
        }
        if (factor < -1) {
            if (height(node.right.right) < height(node.right.left)) {
                node.right = rotateRight(node.right);
            }
            return rotateLeft(node);
        }
        return node;
    }

    private static Node insert(Node node, int key) {
        if (node == null) {
            return new Node(key);
        }
        if (key < node.key) {
            node.left = insert(node.left, key);
        } else if (key > node.key) {
            node.right = insert(node.right, key);
        } else {
            return node;
        }
        return balance(node);
    }

    public void insert(int key) {
        root = insert(root, key);
    }

    private static void inorder(Node node, List<Integer> out) {
        if (node == null) {
            return;
        }
        inorder(node.left, out);
        out.add(node.key);
        inorder(node.right, out);
    }

    public List<Integer> inorder() {
        List<Integer> out = new ArrayList<>();
        inorder(root, out);
        return out;
    }

    public static void main(String[] args) {
        AVLTree tree = new AVLTree();
        for (int key : new int[] {10, 20, 30, 40, 50, 25}) {
            tree.insert(key);
        }
        List<Integer> out = tree.inorder();
        for (int i = 1; i < out.size(); i++) {
            if (out.get(i - 1) > out.get(i)) {
                throw new AssertionError("not sorted");
            }
        }
        System.out.println("avl tree ok");
    }
}
