function bfs(graph, start) {
  const visited = new Set(), queue = [start], order = [];
  while (queue.length) {
    const node = queue.shift();
    if (!visited.has(node)) { visited.add(node); order.push(node); queue.push(...(graph[node]||[])); }
  }
  return order;
}
module.exports = { bfs };