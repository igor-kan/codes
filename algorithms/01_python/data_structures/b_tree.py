"""B-tree of minimum degree t with insert and search."""
class BTreeNode:
    def __init__(self, leaf: bool = True) -> None:
        self.keys: list[int] = []
        self.children: list["BTreeNode"] = []
        self.leaf = leaf


class BTree:
    def __init__(self, t: int = 2) -> None:
        if t < 2:
            raise ValueError("t must be >= 2")
        self.t = t
        self.root = BTreeNode()

    def search(self, key: int, node: BTreeNode | None = None) -> bool:
        node = node or self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        if node.leaf:
            return False
        return self.search(key, node.children[i])

    def insert(self, key: int) -> None:
        if len(self.root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _split_child(self, parent: BTreeNode, index: int) -> None:
        t = self.t
        child = parent.children[index]
        sibling = BTreeNode(child.leaf)
        parent.keys.insert(index, child.keys[t - 1])
        parent.children.insert(index + 1, sibling)
        sibling.keys = child.keys[t:]
        child.keys = child.keys[: t - 1]
        if not child.leaf:
            sibling.children = child.children[t:]
            child.children = child.children[:t]

    def _insert_non_full(self, node: BTreeNode, key: int) -> None:
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def inorder(self, node: BTreeNode | None = None) -> list[int]:
        node = node or self.root
        result = []
        for i, key in enumerate(node.keys):
            if not node.leaf:
                result.extend(self.inorder(node.children[i]))
            result.append(key)
        if not node.leaf:
            result.extend(self.inorder(node.children[-1]))
        return result


if __name__ == "__main__":
    tree = BTree(t=2)
    keys = [10, 20, 5, 6, 12, 30, 7, 17]
    for key in keys:
        tree.insert(key)
    assert tree.inorder() == sorted(keys)
    assert tree.search(17) and not tree.search(99)
    print("b-tree ok")
