import java.util.*;

public class Huffman {

    private static class Node implements Comparable<Node> {
        final char ch;
        final int freq;
        final Node left, right;

        Node(char ch, int freq, Node left, Node right) {
            this.ch = ch;
            this.freq = freq;
            this.left = left;
            this.right = right;
        }

        boolean isLeaf() {
            return left == null && right == null;
        }

        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.freq, o.freq);
        }
    }

    private static void buildCode(Map<Character, String> map, Node x, String s) {
        if (!x.isLeaf()) {
            buildCode(map, x.left, s + '0');
            buildCode(map, x.right, s + '1');
        } else {
            map.put(x.ch, s);
        }
    }

    public static Node buildTree(String text) {
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : text.toCharArray()) freq.put(c, freq.getOrDefault(c, 0) + 1);

        PriorityQueue<Node> pq = new PriorityQueue<>();
        for (Map.Entry<Character, Integer> e : freq.entrySet()) {
            pq.add(new Node(e.getKey(), e.getValue(), null, null));
        }

        while (pq.size() > 1) {
            Node left = pq.poll();
            Node right = pq.poll();
            pq.add(new Node('\0', left.freq + right.freq, left, right));
        }

        return pq.poll();
    }

    public static String decode(Node root, String encoded) {
        StringBuilder sb = new StringBuilder();
        Node curr = root;
        for (char bit : encoded.toCharArray()) {
            curr = (bit == '0') ? curr.left : curr.right;
            if (curr.isLeaf()) {
                sb.append(curr.ch);
                curr = root;
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String msg = "this is an example for a huffman encoding demonstration";
        Node root = buildTree(msg);

        Map<Character, String> codeMap = new HashMap<>();
        buildCode(codeMap, root, "");

        StringBuilder encoded = new StringBuilder();
        for (char c : msg.toCharArray()) encoded.append(codeMap.get(c));

        String decoded = decode(root, encoded.toString());
        if (!decoded.equals(msg)) {
            throw new AssertionError("Huffman decode mismatch");
        }

        System.out.println("[Java Huffman] Successfully encoded and decoded: " + decoded.length() + " chars.");
    }
}
