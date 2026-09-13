#include <vector>
#include <queue>
#include <unordered_set>
std::vector<int> bfs(const std::vector<std::vector<int>>& g, int s){
    std::unordered_set<int> vis; std::queue<int> q; std::vector<int> order;
    q.push(s);
    while(!q.empty()){int u=q.front();q.pop();
        if(vis.insert(u).second){order.push_back(u); for(int v:g[u]) q.push(v);}}
    return order;
}