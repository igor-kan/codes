class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val, self.left, self.right = val, left, right


def serialize(root: TreeNode | None) -> str:
    if not root:
        return "x"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"


def deserialize(data: str) -> TreeNode | None:
    tokens = iter(data.split(","))

    def build():
        token = next(tokens)
        if token == "x":
            return None
        node = TreeNode(int(token))
        node.left, node.right = build(), build()
        return node

    return build()


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert serialize(deserialize(serialize(root))) == serialize(root)
    print("ok")
