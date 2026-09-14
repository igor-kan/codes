class ListNode:
    def __init__(self, val: int = 0, nxt: "ListNode | None" = None) -> None:
        self.val, self.next = val, nxt


def reverse(head: ListNode | None) -> ListNode | None:
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev


if __name__ == "__main__":
    node = ListNode(1, ListNode(2, ListNode(3)))
    out = reverse(node)
    assert [out.val, out.next.val, out.next.next.val] == [3, 2, 1]
    print("ok")
