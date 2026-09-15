public final class EggDrop {
    private EggDrop() {}

    public static void main(String[] args) {
        int eggs = 2;
        int floors = 100;
        int[][] dp = new int[101][eggs + 1];
        int trials = 0;
        while (dp[trials][eggs] < floors) {
            trials++;
            for (int k = 1; k <= eggs; k++) {
                dp[trials][k] = dp[trials - 1][k - 1] + dp[trials - 1][k] + 1;
            }
        }
        if (trials != 14) {
            throw new AssertionError("expected 14 trials");
        }
        System.out.println("egg drop=" + trials);
    }
}
