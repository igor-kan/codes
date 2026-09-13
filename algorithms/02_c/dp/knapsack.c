#include <stdio.h>
int knapsack(int W, int wt[], int val[], int n){
    int dp[n+1][W+1];
    for(int i=0;i<=n;i++) for(int w=0;w<=W;w++){
        dp[i][w]=i==0||w==0?0:dp[i-1][w];
        if(i>0&&wt[i-1]<=w){
            int take=dp[i-1][w-wt[i-1]]+val[i-1];
            if(take>dp[i][w]) dp[i][w]=take;
        }
    }
    return dp[n][W];
}
