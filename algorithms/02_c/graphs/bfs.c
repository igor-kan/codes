#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXV 100
void bfs(int adj[][MAXV], int n, int src) {
    int visited[MAXV]={0}, queue[MAXV], front=0, rear=0;
    visited[src]=1; queue[rear++]=src;
    while(front<rear) {
        int u=queue[front++]; printf("%d ",u);
        for(int v=0;v<n;v++) if(adj[u][v]&&!visited[v]){visited[v]=1;queue[rear++]=v;}
    }
}
