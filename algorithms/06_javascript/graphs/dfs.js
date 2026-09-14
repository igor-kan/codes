function dfs(graph, start) {
  const visited = new Set(), stack = [start], order = [];
  while (stack.length) {
    const node = stack.pop();
    if (!visited.has(node)) {
      visited.add(node);
      order.push(node);
      const neighbors = graph[node] || [];
      for (let i = neighbors.length - 1; i >= 0; i--) stack.push(neighbors[i]);
    }
  }
  return order;
}

const graph = { 0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1], 5: [2] };
const order = dfs(graph, 0);
if (order.length !== 6 || order[0] !== 0) throw new Error("unexpected traversal");
console.log(`[JavaScript DFS] Iterative stack-based traversal verified: [${order.join(", ")}]`);

module.exports = { dfs };
