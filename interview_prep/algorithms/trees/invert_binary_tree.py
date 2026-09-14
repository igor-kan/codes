class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val, self.left, self.right = val, left, right


def invert(root: TreeNode | None) -> TreeNode | None:
    if root:
        root.left, root.right = invert(root.right), invert(root.left)
    return root


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    invert(root)
    assert root.left.val == 3 and root.right.val == 2
    print("ok")
