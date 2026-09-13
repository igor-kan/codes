#include <vector>
#include <algorithm>
int knapsack(const std::vector<int>& w, const std::vector<int>& v, int cap){
    std::vector<int> dp(cap+1,0);
    for(size_t i=0;i<w.size();i++) for(int c=cap;c>=w[i];c--) dp[c]=std::max(dp[c],dp[c-w[i]]+v[i]);
    return dp[cap];
}