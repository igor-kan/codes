"""Aho-Corasick multi-pattern matching."""
from collections import deque


class AhoCorasick:
    def __init__(self, patterns: list[str]) -> None:
        self.goto: list[dict[str, int]] = [{}]
        self.fail: list[int] = [0]
        self.out: list[list[str]] = [[]]
        for pattern in patterns:
            self._insert(pattern)
        self._build()

    def _insert(self, pattern: str) -> None:
        node = 0
        for ch in pattern:
            if ch not in self.goto[node]:
                self.goto[node][ch] = len(self.goto)
                self.goto.append({})
                self.fail.append(0)
                self.out.append([])
            node = self.goto[node][ch]
        self.out[node].append(pattern)

    def _build(self) -> None:
        queue = deque()
        for child in self.goto[0].values():
            queue.append(child)
        while queue:
            node = queue.popleft()
            for ch, nxt in self.goto[node].items():
                queue.append(nxt)
                fallback = self.fail[node]
                while fallback and ch not in self.goto[fallback]:
                    fallback = self.fail[fallback]
                self.fail[nxt] = self.goto[fallback].get(ch, 0)
                self.out[nxt] += self.out[self.fail[nxt]]

    def search(self, text: str) -> list[str]:
        node = 0
        found = []
        for ch in text:
            while node and ch not in self.goto[node]:
                node = self.fail[node]
            node = self.goto[node].get(ch, 0)
            found.extend(self.out[node])
        return found


if __name__ == "__main__":
    machine = AhoCorasick(["he", "she", "his", "hers"])
    assert sorted(machine.search("ushers")) == ["he", "hers", "she"]
    print("aho-corasick ok")
