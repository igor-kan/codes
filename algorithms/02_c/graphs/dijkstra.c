#include <stdio.h>
#include <limits.h>
#define MAXV 100
void dijkstra(int graph[][MAXV], int n, int src) {
    int dist[MAXV], visited[MAXV]={0};
    for(int i=0;i<n;i++) dist[i]=INT_MAX;
    dist[src]=0;
    for(int i=0;i<n-1;i++){
        int u=-1;
        for(int v=0;v<n;v++) if(!visited[v]&&(u==-1||dist[v]<dist[u])) u=v;
        visited[u]=1;
        for(int v=0;v<n;v++)
            if(graph[u][v]&&!visited[v]&&dist[u]+graph[u][v]<dist[v])
                dist[v]=dist[u]+graph[u][v];
    }
    for(int i=0;i<n;i++) printf("dist[%d]=%d\n",i,dist[i]);
}
