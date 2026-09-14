class ListNode:
    def __init__(self, val: int = 0, nxt: "ListNode | None" = None) -> None:
        self.val, self.next = val, nxt


def remove_nth(head: ListNode, n: int) -> ListNode | None:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return dummy.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    out = remove_nth(head, 2)
    vals = []
    while out:
        vals.append(out.val)
        out = out.next
    assert vals == [1, 2, 3, 5]
    print("ok")
