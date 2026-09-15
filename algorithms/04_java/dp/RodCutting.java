// Rod cutting (CLRS 15.1).
public class RodCutting {
    static int cutRod(int[] prices, int n) {
        int[] best = new int[n + 1];
        for (int len = 1; len <= n; len++) {
            for (int i = 1; i <= len; i++) {
                best[len] = Math.max(best[len], prices[i - 1] + best[len - i]);
            }
        }
        return best[n];
    }

    public static void main(String[] args) {
        int[] prices = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30};
        assert cutRod(prices, 4) == 10;
        assert cutRod(prices, 7) == 18;
        assert cutRod(prices, 10) == 30;
        System.out.println("rod cutting ok");
    }
}
