#include <vector>
#include <queue>
#include <climits>
using PII=std::pair<int,int>;
std::vector<int> dijkstra(const std::vector<std::vector<PII>>& g, int src){
    int n=g.size(); std::vector<int> dist(n,INT_MAX); dist[src]=0;
    std::priority_queue<PII,std::vector<PII>,std::greater<>> pq; pq.push({0,src});
    while(!pq.empty()){auto[d,u]=pq.top();pq.pop();
        if(d>dist[u]) continue;
        for(auto[v,w]:g[u]) if(dist[u]+w<dist[v]){dist[v]=dist[u]+w;pq.push({dist[v],v});}}
    return dist;
}