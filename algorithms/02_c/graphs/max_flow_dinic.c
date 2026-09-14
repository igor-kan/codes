#include <stdio.h>
#include <string.h>

#define MAXN 100
#define MAXM 1000

typedef struct { int to, cap, next; } Edge;

static Edge edges[2 * MAXM];
static int head[MAXN];
static int edge_cnt;
static int level[MAXN];
static int it[MAXN];
static int q[MAXN];

static void add_edge(int u, int v, int cap) {
    edges[edge_cnt].to = v; edges[edge_cnt].cap = cap; edges[edge_cnt].next = head[u]; head[u] = edge_cnt++;
    edges[edge_cnt].to = u; edges[edge_cnt].cap = 0;  edges[edge_cnt].next = head[v]; head[v] = edge_cnt++;
}

static int bfs(int s, int t, int n) {
    memset(level, -1, sizeof(level));
    int front = 0, rear = 0;
    level[s] = 0;
    q[rear++] = s;
    while (front < rear) {
        int u = q[front++];
        for (int e = head[u]; e != -1; e = edges[e].next) {
            int v = edges[e].to;
            if (edges[e].cap > 0 && level[v] == -1) {
                level[v] = level[u] + 1;
                q[rear++] = v;
            }
        }
    }
    return level[t] != -1;
}

static int dfs(int u, int t, int f) {
    if (u == t) return f;
    for (int *e = &it[u]; *e != -1; *e = edges[*e].next) {
        int v = edges[*e].to;
        if (edges[*e].cap > 0 && level[v] == level[u] + 1) {
            int pushed = dfs(v, t, f < edges[*e].cap ? f : edges[*e].cap);
            if (pushed > 0) {
                edges[*e].cap -= pushed;
                edges[*e ^ 1].cap += pushed;
                return pushed;
            }
        }
    }
    return 0;
}

int dinic(int s, int t, int n) {
    int flow = 0;
    while (bfs(s, t, n)) {
        for (int i = 0; i < n; ++i) it[i] = head[i];
        int pushed;
        while ((pushed = dfs(s, t, __INT_MAX__)) > 0) flow += pushed;
    }
    return flow;
}

int main(void) {
    edge_cnt = 0;
    memset(head, -1, sizeof(head));

    add_edge(0, 1, 10);
    add_edge(0, 2, 5);
    add_edge(1, 2, 15);
    add_edge(1, 3, 5);
    add_edge(2, 3, 10);

    int flow = dinic(0, 3, 4);
    if (flow != 15) {
        printf("[C Dinic] FAILED: max flow %d, want 15\n", flow);
        return 1;
    }
    printf("[C Dinic] Max flow verified (=15)\n");
    return 0;
}
