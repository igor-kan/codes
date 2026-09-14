class ListNode:
    def __init__(self, val: int = 0, nxt: "ListNode | None" = None) -> None:
        self.val, self.next = val, nxt


def reorder(head: ListNode) -> None:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    prev, cur = None, slow
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    first, second = head, prev
    while second.next:
        first.next, second.next = second, first.next
        first, second = first.next.next if first.next else None, second.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    reorder(head)
    vals, cur = [], head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    assert vals == [1, 4, 2, 3]
    print("ok")
