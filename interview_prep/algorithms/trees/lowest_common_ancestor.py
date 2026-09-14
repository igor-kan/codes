class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val, self.left, self.right = val, left, right


def lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    while (root.val - p.val) * (root.val - q.val) > 0:
        root = root.left if p.val < root.val else root.right
    return root


if __name__ == "__main__":
    p, q = TreeNode(2), TreeNode(8)
    root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4)), TreeNode(8, None, TreeNode(9)))
    assert lca(root, p, q).val == 6
    print("ok")
