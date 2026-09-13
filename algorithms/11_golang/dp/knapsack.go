package dp
func Knapsack(weights,values []int, cap int) int {
	n:=len(weights); dp:=make([]int,cap+1)
	for i:=0;i<n;i++ { for w:=cap;w>=weights[i];w-- {
		if v:=dp[w-weights[i]]+values[i];v>dp[w] { dp[w]=v } } }
	return dp[cap]
}