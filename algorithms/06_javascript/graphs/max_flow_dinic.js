class Dinic {
  constructor(n) {
    this.n = n;
    this.graph = Array.from({ length: n }, () => []);
  }
  addEdge(u, v, cap) {
    this.graph[u].push({ to: v, cap, rev: this.graph[v].length });
    this.graph[v].push({ to: u, cap: 0, rev: this.graph[u].length - 1 });
  }
  bfs(s, t) {
    this.level = new Array(this.n).fill(-1);
    this.level[s] = 0;
    const q = [s];
    while (q.length) {
      const u = q.shift();
      for (const e of this.graph[u]) {
        if (e.cap > 0 && this.level[e.to] < 0) {
          this.level[e.to] = this.level[u] + 1;
          q.push(e.to);
        }
      }
    }
    return this.level[t] >= 0;
  }
  dfs(u, t, f) {
    if (u === t) return f;
    for (; this.it[u] < this.graph[u].length; this.it[u]++) {
      const e = this.graph[u][this.it[u]];
      if (e.cap > 0 && this.level[e.to] === this.level[u] + 1) {
        const d = this.dfs(e.to, t, Math.min(f, e.cap));
        if (d > 0) {
          e.cap -= d;
          this.graph[e.to][e.rev].cap += d;
          return d;
        }
      }
    }
    return 0;
  }
  maxFlow(s, t) {
    let flow = 0;
    const INF = Infinity;
    while (this.bfs(s, t)) {
      this.it = new Array(this.n).fill(0);
      let f;
      while ((f = this.dfs(s, t, INF)) > 0) flow += f;
    }
    return flow;
  }
}

module.exports = { Dinic };

if (require.main === module) {
  const dinic = new Dinic(4);
  dinic.addEdge(0, 1, 3);
  dinic.addEdge(0, 2, 2);
  dinic.addEdge(1, 2, 1);
  dinic.addEdge(1, 3, 2);
  dinic.addEdge(2, 3, 2);
  if (dinic.maxFlow(0, 3) !== 4) throw new Error("dinic max flow failed");
  console.log("[JavaScript Dinic Max Flow] Dinic's algorithm verified");
}
