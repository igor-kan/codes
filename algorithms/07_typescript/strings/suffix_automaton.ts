/**
 * Suffix Automaton (Directed Acyclic Word Graph)
 * Linear-time and linear-space O(n) compact representation of all substrings of a string.
 */

class State {
  len = 0;
  link = -1;
  next = new Map<string, number>();
}

export class SuffixAutomaton {
  states: State[] = [];
  last = 0;

  constructor() {
    const init = new State();
    this.states.push(init);
  }

  extend(c: string): void {
    const cur = this.states.length;
    const curState = new State();
    curState.len = this.states[this.last].len + 1;
    this.states.push(curState);

    let p = this.last;
    while (p !== -1 && !this.states[p].next.has(c)) {
      this.states[p].next.set(c, cur);
      p = this.states[p].link;
    }

    if (p === -1) {
      curState.link = 0;
    } else {
      const q = this.states[p].next.get(c)!;
      if (this.states[p].len + 1 === this.states[q].len) {
        curState.link = q;
      } else {
        const clone = this.states.length;
        const cloneState = new State();
        cloneState.len = this.states[p].len + 1;
        cloneState.next = new Map(this.states[q].next);
        cloneState.link = this.states[q].link;
        this.states.push(cloneState);

        while (p !== -1 && this.states[p].next.get(c) === q) {
          this.states[p].next.set(c, clone);
          p = this.states[p].link;
        }
        this.states[q].link = clone;
        curState.link = clone;
      }
    }
    this.last = cur;
  }

  contains(pattern: string): boolean {
    let p = 0;
    for (const ch of pattern) {
      if (!this.states[p].next.has(ch)) return false;
      p = this.states[p].next.get(ch)!;
    }
    return true;
  }
}

const sam = new SuffixAutomaton();
for (const ch of "abracadabra") sam.extend(ch);
if (!sam.contains("cadabra") || sam.contains("xyz")) {
  throw new Error("Suffix Automaton failed");
}
console.log("Suffix Automaton verified successfully.");
