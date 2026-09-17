package data_structures;

import java.util.Random;

/**
 * Skip List in Java (William Pugh).
 */
public class SkipList {
    private static class Node {
        int val;
        Node[] forward;
        Node(int val, int level) {
            this.val = val;
            this.forward = new Node[level + 1];
        }
    }

    private final Node head = new Node(-1, 16);
    private int level = 0;
    private final Random rand = new Random();

    public void insert(int val) {
        Node[] update = new Node[16];
        Node curr = head;
        for (int i = level; i >= 0; i--) {
            while (curr.forward[i] != null && curr.forward[i].val < val) {
                curr = curr.forward[i];
            }
            update[i] = curr;
        }
        int lvl = 0;
        while (rand.nextDouble() < 0.5 && lvl < 15) lvl++;
        Node newNode = new Node(val, lvl);
        for (int i = 0; i <= lvl; i++) {
            newNode.forward[i] = update[i].forward[i];
            update[i].forward[i] = newNode;
        }
    }

    public boolean search(int val) {
        Node curr = head;
        for (int i = level; i >= 0; i--) {
            while (curr.forward[i] != null && curr.forward[i].val < val) {
                curr = curr.forward[i];
            }
        }
        curr = curr.forward[0];
        return curr != null && curr.val == val;
    }

    public static void main(String[] args) {
        SkipList sl = new SkipList();
        sl.insert(42);
        assert sl.search(42);
        System.out.println("Java Skip List verified.");
    }
}
