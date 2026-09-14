"""Probabilistic skip list."""
import random


class Node:
    def __init__(self, value: int, level: int) -> None:
        self.value = value
        self.forward = [None] * (level + 1)


class SkipList:
    def __init__(self, max_level: int = 16, probability: float = 0.5) -> None:
        self.max_level = max_level
        self.probability = probability
        self.level = 0
        self.header = Node(-1, max_level)

    def _random_level(self) -> int:
        level = 0
        while random.random() < self.probability and level < self.max_level:
            level += 1
        return level

    def insert(self, value: int) -> None:
        update = [None] * (self.max_level + 1)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        level = self._random_level()
        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.header
            self.level = level
        node = Node(value, level)
        for i in range(level + 1):
            node.forward[i] = update[i].forward[i]
            update[i].forward[i] = node

    def contains(self, value: int) -> bool:
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        return bool(current and current.value == value)


if __name__ == "__main__":
    random.seed(0)
    skiplist = SkipList()
    for value in [3, 6, 7, 9, 12, 19, 17]:
        skiplist.insert(value)
    assert skiplist.contains(19) and not skiplist.contains(5)
    print("ok")
