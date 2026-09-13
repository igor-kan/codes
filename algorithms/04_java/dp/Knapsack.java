public class Knapsack {
    public static int knapsack(int[] w, int[] v, int cap){
        int n=w.length; int[] dp=new int[cap+1];
        for(int i=0;i<n;i++) for(int c=cap;c>=w[i];c--) dp[c]=Math.max(dp[c],dp[c-w[i]]+v[i]);
        return dp[cap];
    }
}