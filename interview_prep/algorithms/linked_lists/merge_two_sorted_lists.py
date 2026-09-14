class ListNode:
    def __init__(self, val: int = 0, nxt: "ListNode | None" = None) -> None:
        self.val, self.next = val, nxt


def merge(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


if __name__ == "__main__":
    a, b = ListNode(1, ListNode(3)), ListNode(2, ListNode(4))
    out = merge(a, b)
    vals = []
    while out:
        vals.append(out.val)
        out = out.next
    assert vals == [1, 2, 3, 4]
    print("ok")
