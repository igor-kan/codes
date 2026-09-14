class ListNode:
    def __init__(self, val: int = 0, nxt: "ListNode | None" = None) -> None:
        self.val, self.next = val, nxt


def has_cycle(head: ListNode | None) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    a, b, c = ListNode(1), ListNode(2), ListNode(3)
    a.next, b.next, c.next = b, c, b
    assert has_cycle(a)
    print("ok")
