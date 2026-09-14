class Node:
    def __init__(self, val: int = 0, neighbors: list["Node"] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors or []


def clone_graph(node: Node | None) -> Node | None:
    if not node:
        return None
    clones: dict[int, Node] = {}

    def dfs(n: Node) -> Node:
        if n.val in clones:
            return clones[n.val]
        copy = Node(n.val)
        clones[n.val] = copy
        copy.neighbors = [dfs(neighbor) for neighbor in n.neighbors]
        return copy

    return dfs(node)


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    a.neighbors = [b]
    b.neighbors = [a]
    clone = clone_graph(a)
    assert clone is not a and clone.neighbors[0].val == 2
    print("ok")
