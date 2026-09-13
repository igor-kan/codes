export function bfs(graph: Map<number,number[]>, start: number): number[] {
  const visited = new Set<number>(), queue = [start], order: number[] = [];
  while (queue.length) {
    const node = queue.shift()!;
    if (!visited.has(node)) { visited.add(node); order.push(node); queue.push(...(graph.get(node)??[])); }
  }
  return order;
}