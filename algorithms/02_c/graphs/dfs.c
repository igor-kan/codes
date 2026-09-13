#include <stdio.h>
#define MAXV 100
int visited[MAXV];
void dfs(int adj[][MAXV], int n, int u) {
    visited[u]=1; printf("%d ",u);
    for(int v=0;v<n;v++) if(adj[u][v]&&!visited[v]) dfs(adj,n,v);
}
