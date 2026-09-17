/**
 * 2-SAT Solver
 * Solves 2-Satisfiability in O(V + E) using implication graph and Tarjan SCC.
 */

export class TwoSatSolver {
  private n: number;
  private adj: number[][];

  constructor(variables: number) {
    this.n = variables;
    this.adj = Array.from({ length: 2 * variables }, () => []);
  }

  // literal > 0 means x_i, literal < 0 means ~x_i (1-indexed)
  addClause(u: number, v: number): void {
    const notU = -u;
    const notV = -v;
    this.adj[this.toIndex(notU)].push(this.toIndex(v));
    this.adj[this.toIndex(notV)].push(this.toIndex(u));
  }

  private toIndex(literal: number): number {
    return literal > 0 ? literal - 1 : this.n + (-literal - 1);
  }

  solve(): boolean[] | null {
    const total = 2 * this.n;
    const index = new Array(total).fill(-1);
    const lowlink = new Array(total).fill(-1);
    const onStack = new Array(total).fill(false);
    const stack: number[] = [];
    const comp = new Array(total).fill(-1);
    let curIndex = 0;
    let compCount = 0;

    const dfs = (v: number) => {
      index[v] = lowlink[v] = curIndex++;
      stack.push(v);
      onStack[v] = true;
      for (const to of this.adj[v]) {
        if (index[to] === -1) {
          dfs(to);
          lowlink[v] = Math.min(lowlink[v], lowlink[to]);
        } else if (onStack[to]) {
          lowlink[v] = Math.min(lowlink[v], index[to]);
        }
      }
      if (lowlink[v] === index[v]) {
        while (true) {
          const w = stack.pop()!;
          onStack[w] = false;
          comp[w] = compCount;
          if (w === v) break;
        }
        compCount++;
      }
    };

    for (let i = 0; i < total; i++) {
      if (index[i] === -1) dfs(i);
    }

    const assignment = new Array(this.n).fill(false);
    for (let i = 0; i < this.n; i++) {
      if (comp[i] === comp[i + this.n]) return null; // Unsatisfiable
      assignment[i] = comp[i] < comp[i + this.n];
    }
    return assignment;
  }
}

const sat = new TwoSatSolver(2);
sat.addClause(1, 2);   // (x1 or x2)
sat.addClause(-1, 2);  // (~x1 or x2)
sat.addClause(1, -2);  // (x1 or ~x2)
const sol = sat.solve();
if (!sol || !sol[0] || !sol[1]) throw new Error("2-SAT solver failed");
console.log("2-SAT Solver verified successfully.");
