from collections import defaultdict, deque


def alien_order(words: list[str]) -> str:
    graph: dict[str, set[str]] = {c: set() for word in words for c in word}
    indegree = defaultdict(int)
    for first, second in zip(words, words[1:]):
        for a, b in zip(first, second):
            if a != b:
                if b not in graph[a]:
                    graph[a].add(b)
                    indegree[b] += 1
                break
        else:
            if len(second) < len(first):
                return ""
    queue = deque(c for c in graph if indegree[c] == 0)
    order = []
    while queue:
        ch = queue.popleft()
        order.append(ch)
        for nxt in graph[ch]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return "".join(order) if len(order) == len(graph) else ""


if __name__ == "__main__":
    assert alien_order(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
    print("ok")
