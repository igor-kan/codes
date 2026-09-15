"""Suffix automaton: count distinct substrings."""
class SuffixAutomaton:
    def __init__(self) -> None:
        self.next: list[dict[str, int]] = [{}]
        self.link = [-1]
        self.length = [0]
        self.last = 0

    def extend(self, ch: str) -> None:
        cur = len(self.length)
        self.length.append(self.length[self.last] + 1)
        self.next.append({})
        self.link.append(0)
        p = self.last
        while p != -1 and ch not in self.next[p]:
            self.next[p][ch] = cur
            p = self.link[p]
        if p == -1:
            self.link[cur] = 0
        else:
            q = self.next[p][ch]
            if self.length[p] + 1 == self.length[q]:
                self.link[cur] = q
            else:
                clone = len(self.length)
                self.length.append(self.length[p] + 1)
                self.next.append(dict(self.next[q]))
                self.link.append(self.link[q])
                while p != -1 and self.next[p].get(ch) == q:
                    self.next[p][ch] = clone
                    p = self.link[p]
                self.link[q] = self.link[cur] = clone
        self.last = cur

    def distinct_substrings(self) -> int:
        return sum(self.length[i] - self.length[self.link[i]] for i in range(1, len(self.length)))


def count_distinct_substrings(text: str) -> int:
    automaton = SuffixAutomaton()
    for ch in text:
        automaton.extend(ch)
    return automaton.distinct_substrings()


if __name__ == "__main__":
    assert count_distinct_substrings("ababa") == 9
    print("suffix automaton ok")
