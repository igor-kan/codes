#include <stdio.h>
#include <string.h>
#define MAX 1001
int lcs(const char *a, const char *b){
    int m=strlen(a), n=strlen(b);
    static int dp[MAX][MAX];
    for(int i=0;i<=m;i++) for(int j=0;j<=n;j++){
        if(!i||!j) dp[i][j]=0;
        else if(a[i-1]==b[j-1]) dp[i][j]=dp[i-1][j-1]+1;
        else dp[i][j]=dp[i-1][j]>dp[i][j-1]?dp[i-1][j]:dp[i][j-1];
    }
    return dp[m][n];
}
