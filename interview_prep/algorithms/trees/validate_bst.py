class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val, self.left, self.right = val, left, right


def is_valid_bst(root: TreeNode | None, low=float("-inf"), high=float("inf")) -> bool:
    if not root:
        return True
    if not low < root.val < high:
        return False
    return is_valid_bst(root.left, low, root.val) and is_valid_bst(root.right, root.val, high)


if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(root)
    print("ok")
