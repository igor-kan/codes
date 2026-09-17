/**
 * Aho-Corasick Automaton
 * Multi-pattern dictionary-matching algorithm with linear construction O(sum(m)) and search O(n + z).
 */

class ACNode {
  children = new Map<string, ACNode>();
  fail: ACNode | null = null;
  output: string[] = [];
}

export class AhoCorasick {
  root = new ACNode();

  constructor(patterns: string[]) {
    this.buildTrie(patterns);
    this.buildFailureLinks();
  }

  private buildTrie(patterns: string[]): void {
    for (const pat of patterns) {
      let curr = this.root;
      for (const ch of pat) {
        if (!curr.children.has(ch)) {
          curr.children.set(ch, new ACNode());
        }
        curr = curr.children.get(ch)!;
      }
      curr.output.push(pat);
    }
  }

  private buildFailureLinks(): void {
    const queue: ACNode[] = [];
    for (const child of this.root.children.values()) {
      child.fail = this.root;
      queue.push(child);
    }

    while (queue.length > 0) {
      const curr = queue.shift()!;
      for (const [ch, child] of curr.children.entries()) {
        let f = curr.fail;
        while (f && !f.children.has(ch)) f = f.fail;
        child.fail = f ? f.children.get(ch)! : this.root;
        child.output.push(...child.fail.output);
        queue.push(child);
      }
    }
  }

  search(text: string): { pattern: string; index: number }[] {
    const matches: { pattern: string; index: number }[] = [];
    let curr: ACNode | null = this.root;

    for (let i = 0; i < text.length; i++) {
      const ch = text[i];
      while (curr && !curr.children.has(ch)) curr = curr.fail;
      curr = curr ? curr.children.get(ch)! : this.root;

      for (const pat of curr.output) {
        matches.push({ pattern: pat, index: i - pat.length + 1 });
      }
    }
    return matches;
  }
}

const ac = new AhoCorasick(["he", "she", "his", "hers"]);
const acMatches = ac.search("ahishers");
if (acMatches.length !== 3) throw new Error("Aho-Corasick failed");
console.log("Aho-Corasick Automaton verified successfully.");
