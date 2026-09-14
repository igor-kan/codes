from collections import deque


def ladder_length(begin: str, end: str, word_list: list[str]) -> int:
    words = set(word_list)
    if end not in words:
        return 0
    queue = deque([(begin, 1)])
    while queue:
        word, steps = queue.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for code in range(ord("a"), ord("z") + 1):
                nxt = word[:i] + chr(code) + word[i + 1:]
                if nxt in words:
                    words.discard(nxt)
                    queue.append((nxt, steps + 1))
    return 0


if __name__ == "__main__":
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    print("ok")
